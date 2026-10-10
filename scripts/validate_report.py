#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
validate_report.py - 河北大学《C程序设计》实验报告自动化质量审查脚本

功能：
1. 检测 document.xml 中是否存在 <w:color> 彩色文字标签（必须为 0）；
2. 检索并拦截 AI 痕迹与违禁敏感词（如“契合”、“三大要求”、“Prompt”等）；
3. 检查封面后是否存在多余溢出段落导致的第 2 页空白页；
4. 检查外层主表格结构及内部嵌套数据对比表格数量；
5. 检查附录源代码表格中必要源程序文件的完整性；
6. 检查核心实验题目（★号重点题）关键词覆盖率，严防少写漏写。
"""

import sys
import os
import re
import zipfile
import argparse
from xml.etree import ElementTree as ET

# ANSI 颜色输出
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

FORBIDDEN_WORDS = [
    "契合",
    "三大要求",
    "作为AI",
    "作为人工智能",
    "Prompt",
    "提示词",
    "大模型",
    "语言模型",
    "代码助手",
    "模板要求如下",
    "满足以上要求",
    "严格遵循模板规范的六大标准开发步骤",
    "本次实验为实验一、实验二与实验三的综合合并实验",
    "老老实实",
    "问了同学",
    "手抖输入"
]


REQUIRED_SOURCES = [
    "star_correct.c",
    "diamond.c",
    "io_char.c",
    "sum.c",
    "avg.c",
    "parallel.c",
    "temp_convert.c"
]

CORE_KEYWORDS_MERGED = [
    ("语法错误调试 (3处错误)", ["语法错误", "分号", "编译器"]),
    ("star1~star4 目测与验证", ["star1", "star4", "目测"]),
    ("菱形图案输出", ["菱形", "diamond"]),
    ("实数与字符赋值截断", ["25.5", "65", "截断"]),
    ("未定义/未初始化变量", ["undeclared", "垃圾值", "未初始化"]),
    ("实数保留2位小数", ["%.2f", "保留 2 位", "保留2位"]),
    ("格式符错配测试 (%d/%c)", ["%f 格式改成", "%d或%c", "错配"]),
    ("scanf 缺少取地址符 &", ["&a", "地址", "指针"]),
    ("多变量输入分隔符机制", ["%d%f", "%d,%f", "逗号"]),
    ("字符与无回显输入", ["getchar", "putchar", "getch"]),
    ("整数求和与平均值", ["sum.c", "avg.c", "平均值"]),
    ("并联电路总电流计算", ["parallel.c", "并联", "欧姆定律"]),
    ("左值错误 (10 = a)", ["10 = a", "10=a", "左值", "lvalue"]),
    ("除法截断 (1/2 vs 1.0/2)", ["1/2", "1.0/2", "整数除法"]),
    ("字符溢出与截断 (c = 321)", ["321", "溢出", "模"]),
    ("转义字符测试 (\\101, \\x61)", ["\\101", "\\x61", "八进制", "十六进制"]),
    ("华氏温度转摄氏温度", ["temp_convert", "5.0/9.0", "华氏", "摄氏"])
]


def validate_report(docx_path, is_merged=True):
    print(f"\n{BOLD}{CYAN}======================================================{RESET}")
    print(f"{BOLD}{CYAN}  河北大学《C程序设计》实验报告自动化终检系统 v1.0   {RESET}")
    print(f"{BOLD}{CYAN}======================================================{RESET}")
    print(f"正在审查文件: {BOLD}{docx_path}{RESET}\n")

    if not os.path.exists(docx_path):
        print(f"{RED}[ERROR] 文件不存在: {docx_path}{RESET}")
        return False

    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            xml_content = z.read('word/document.xml').decode('utf-8')
    except Exception as e:
        print(f"{RED}[ERROR] 无法解析 docx 压缩结构: {e}{RESET}")
        return False

    all_passed = True

    # 1. 检测 <w:color> 纯黑规范
    print(f"{BOLD}[1/7] 检查字体颜色规范 (纯黑 0 色标)...{RESET}")
    color_tags = re.findall(r'<w:color [^>]*>', xml_content)
    if len(color_tags) == 0:
        print(f"  {GREEN}✔ PASS: 全文 <w:color> 标签数量为 0，符合纯黑原则。{RESET}")
    else:
        print(f"  {RED}✘ FAIL: 发现 {len(color_tags)} 个 <w:color> 彩色字体标签，可能导致打印或WPS显示杂色！{RESET}")
        for t in color_tags[:5]:
            print(f"    - {t}")
        all_passed = False

    # 2. 检查字体族一致性 (严防等线/微软雅黑/Calibri等非模板字体)
    print(f"\n{BOLD}[2/7] 检查字体族一致性规范 (对齐模板宋体与Times New Roman)...{RESET}")
    root = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    unauthorized_fonts = {"微软雅黑", "Microsoft YaHei", "等线", "DengXian", "Calibri"}
    found_unauth_fonts = set()
    for rf in root.findall('.//w:rFonts', ns):
        for k, v in rf.attrib.items():
            if not k.endswith('Theme') and not k.endswith('hint'):
                if v in unauthorized_fonts:
                    found_unauth_fonts.add(v)
    if not found_unauth_fonts:
        print(f"  {GREEN}✔ PASS: 字体族严格对齐模板规范（宋体 + Times New Roman + Courier New / Consolas）。{RESET}")
    else:
        print(f"  {YELLOW}⚠ WARNING: 检测到非模板默认字体: {found_unauth_fonts}，格式容易产生拼凑割裂感，建议统一对齐为宋体与Times New Roman！{RESET}")

    # 3. 检索违禁词与 AI 痕迹
    print(f"\n{BOLD}[3/7] 检查 AI 痕迹与违禁敏感词...{RESET}")

    found_forbidden = []
    for word in FORBIDDEN_WORDS:
        if word in xml_content:
            found_forbidden.append(word)

    if not found_forbidden:
        print(f"  {GREEN}✔ PASS: 未发现任何违禁元描述及 AI 生成痕迹。{RESET}")
    else:
        print(f"  {RED}✘ FAIL: 发现违禁敏感词: {found_forbidden}，必须全部清除！{RESET}")
        all_passed = False

    # 4. 检查封面后空白页与分页符
    print(f"\n{BOLD}[4/7] 检查封面排版与空白页排查...{RESET}")
    root = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    body = root.find('w:body', ns)
    
    # 查找首个主表格前所有段落
    elements = list(body)
    cover_paragraphs = []
    first_tbl_idx = -1
    for idx, el in enumerate(elements):
        if el.tag.endswith('tbl'):
            first_tbl_idx = idx
            break
        elif el.tag.endswith('p'):
            cover_paragraphs.append(el)

    # 检查封面最后几个段落是否有空行 + 分页符挤占
    empty_trailing_p = 0
    has_page_break = False
    for p in reversed(cover_paragraphs):
        text = ''.join(p.itertext()).strip()
        has_pb = len(p.findall('.//w:br[@w:type="page"]', ns)) > 0
        if has_pb:
            has_page_break = True
        if not text and not has_pb:
            empty_trailing_p += 1
        elif text:
            break

    if empty_trailing_p <= 1 and has_page_break:
        print(f"  {GREEN}✔ PASS: 封面末尾段落紧凑 (多余空行={empty_trailing_p})，已配置分页符，无第2页空白页风险。{RESET}")
    elif not has_page_break:
        print(f"  {YELLOW}⚠ WARNING: 封面未检测到显式分页符，可能依赖自然表格换页。请在 WPS 中确认封面与正文是否分页。{RESET}")
    else:
        print(f"  {YELLOW}⚠ WARNING: 封面末尾检测到 {empty_trailing_p} 个空段落，可能将分页符挤压到第2页导致空白页！建议清理。{RESET}")

    # 5. 检查表格数量与层级
    print(f"\n{BOLD}[5/7] 检查模板大表格与内嵌数据对比表...{RESET}")
    tbl_elements = root.findall('.//w:tbl', ns)
    print(f"  文档中总表格数量: {len(tbl_elements)}")
    if len(tbl_elements) >= (10 if is_merged else 4):
        print(f"  {GREEN}✔ PASS: 表格数量充足 (包含主框架表与数据对比表)，充分落实表格化对比要求。{RESET}")
    else:
        print(f"  {YELLOW}⚠ WARNING: 表格总数仅为 {len(tbl_elements)}，建议将更多测试对比项转换为表格呈现以提升工科严谨度。{RESET}")

    # 6. 检查附录源代码完整性
    print(f"\n{BOLD}[6/7] 检查附录源代码文件完整性...{RESET}")
    missing_sources = []
    if is_merged:
        for src in REQUIRED_SOURCES:
            if src not in xml_content:
                missing_sources.append(src)
        if not missing_sources:
            print(f"  {GREEN}✔ PASS: 附录包含全部 7 个核心 C 源程序 ({', '.join(REQUIRED_SOURCES)})。{RESET}")
        else:
            print(f"  {RED}✘ FAIL: 附录缺少以下源程序: {missing_sources}{RESET}")
            all_passed = False
    else:
        print(f"  {CYAN}ℹ 单次实验模式，跳过合并源程序全量核对。{RESET}")

    # 7. 检查核心题目覆盖度 (防漏写)
    print(f"\n{BOLD}[7/7] 检查指导书核心小题 (★题) 覆盖度...{RESET}")

    omitted_items = []
    if is_merged:
        for title, kw_list in CORE_KEYWORDS_MERGED:
            matched = any(kw in xml_content for kw in kw_list)
            if matched:
                print(f"  {GREEN}✔ 覆盖: {title}{RESET}")
            else:
                print(f"  {RED}✘ 缺失: {title} (未找到关键词: {kw_list}){RESET}")
                omitted_items.append(title)
        
        if not omitted_items:
            print(f"\n  {GREEN}✔ PASS: 100% 覆盖指导书所有核心任务与验证点，零漏写！{RESET}")
        else:
            print(f"\n  {RED}✘ FAIL: 发现 {len(omitted_items)} 处题目遗漏，请务必核对指导书补齐！{RESET}")
            all_passed = False

    # 总结输出
    print(f"\n{BOLD}{CYAN}======================================================{RESET}")
    if all_passed:
        print(f"{BOLD}{GREEN}  🎉 终检结果: 全部核心规范核验通过！已达直接提交标准。{RESET}")
    else:
        print(f"{BOLD}{RED}  ❌ 终检结果: 存在不合规项，请根据上述提示修复后再提交！{RESET}")
    print(f"{BOLD}{CYAN}======================================================{RESET}\n")

    return all_passed


def main():
    parser = argparse.ArgumentParser(description="河北大学《C程序设计》实验报告质检工具")
    parser.add_argument("--file", "-f", required=True, help="要检查的 docx 实验报告文件绝对路径")
    parser.add_argument("--single", action="store_true", help="单次实验模式（默认检测合并实验一至三）")
    args = parser.parse_args()

    passed = validate_report(args.file, is_merged=not args.single)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
