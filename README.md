# 河北大学《C程序设计》实验报告撰写与排版规范 Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Target: HBU CEIE](https://img.shields.io/badge/Target-HBU_电信学院-red.svg)](http://ceie.hbu.cn/)
[![Zero AI Traces](https://img.shields.io/badge/Style-Zero_AI_Traces-green.svg)](#)
[![Zero Color Tags](https://img.shields.io/badge/OpenXML-Zero_%3Cw%3Acolor%3E-black.svg)](#)
[![Universal Agent](https://img.shields.io/badge/Agent-Universal_Compatibility-blueviolet.svg)](#)

本 Skill 专为**河北大学（HBU）电子信息工程学院《C程序设计》**（课程号：`1326P00001-01`，工科必修课）定制。系统化解决了学生与自动化 AI 工具在编制实验报告（涵盖单次实验及实验一至三合并报告）时遇到的核心痛点：**少写漏写、自作聪明多写、结构打乱无序、AI元描述暴露、彩色字体被抓包、封面后空白页、过程只抄大纲不写实现**等问题。

本项目采用标准 Markdown 规程与模块化设计，**支持所有主流 AI Agent（Claude、Cursor、Cline、Windsurf、ChatGPT/OpenAI、Antigravity CLI 等）通用加载与执行**。

---

## 解决的核心痛点（血泪经验提炼）

在以往由 AI 协助生成或初学者撰写实验报告的过程中，最容易踩中以下几大致命雷区：

1. **少写漏写，偷工减料**：
   - 典型问题：指导书里明确要求的多项带 `★` 的上机验证（如“修改 %f 为 %d 或 %c”、“缺少取地址符 & 导致崩溃”、“实数保留 2 位”等），被草率合并为一句笼统空话，导致扣分。
   - 本项目解法：**全量 Checklist 地毯式扫描**，指导书中每一个小任务、每一个 `★` 必须独立编号、逐题作答。

2. **多写与画蛇添足的 AI 痕迹**：
   - 典型问题：正文中出现诸如“（契合模板三大要求）”、“作为代码助手”、“根据提示词分析”或开篇“本次实验为综合合并实验...严格遵循六大步骤推进...”等荒唐的说明书腔调，被老师直接判定为机器代写。
   - 本项目解法：**严禁元描述黑名单与前言废话**，直接从具体的实验项目和任务开门见山写起，只就事论事记录代码与现象，还原真实普通偏优秀的工科学生自然朴素文风。
3. **结构混乱，不按指导书出牌**：
   - 典型问题：打乱指导书固有层级，私自合并跨章节内容或自创自排序号。
   - 本项目解法：**100% 对齐原版指导书目录树**，保持 `一、实验项目... -> 1. -> (1) -> ★` 的标准工科顺序。


4. **实验目的自作聪明改写**：
   - 典型问题：自作主张扩写为高深假大空的学术论文腔。
   - 本项目解法：**100% 逐字原句复制指导书原句**（包括序号与标点），像真人复制粘贴一样自然真实。
5. **过程只抄题目大纲，缺乏代码实现**：
   - 典型问题：在“实验过程及代码实现”中只敷衍罗列题目，没有具体的算法设计和核心代码。
   - 本项目解法：**实打实写入【算法设计】与【核心代码实现】**，落实输入输出定义、公式推导、整除截断防坑细节与精简可编译 C 源码。
6. **文字堆砌，缺乏表格**：
   - 典型问题：控制台输出与测试数据全是纯文字，排版松散。
   - 本项目解法：**全面表格化（Table-First）**，内置 9 大类数据对比表（输入输出对照、格式符错配、溢出与截断、报错原因剖析等）。
7. **彩色字体与排版翻车**：
   - 典型问题：Word/WPS 渲染出刺眼的蓝字/棕字（包含 `<w:color>`），封面后挤出多余的空白第 2 页。
   - 本项目解法：**纯黑 0 色标规范**，消除封面末尾多余回车符，封面直通正文大表。
8. **字体割裂与非模板字体翻车**：
   - 典型问题：其他 AI 生成或修改 docx 时，默认套用等线（DengXian）、微软雅黑（Microsoft YaHei）或 Calibri，导致正文与原模板传统公文体（宋体 + Times New Roman）产生强烈割裂。
   - 本项目解法：**全量 1:1 严格继承模板字体族**，中文统一宋体（SimSun），西文统一 Times New Roman，代码统一 Courier New / Consolas，正文字号严格为小四（12pt / sz=24）或五号（10.5pt / sz=21）。
9. **打散主表导致模板结构失效**：
   - 典型问题：其他 AI 生成时将原模板外层主表格打散为散碎的独立段落或私自重构表格体系，彻底破坏学院官方模板框架。
   - 本项目解法：**严禁打散或重组原模板主表格**，完整保留原模板 6 大核心板块（实验名称、实验目的、实验环境及工具、实验过程及代码实现、实验结果及结果分析、实验总结和反思）及附录代码大表格，所有内容与嵌套子表全部规范嵌入对应单元格中。
10. **语调两极化失衡：非生硬工程手册即做作幼儿日记**：
   - 典型问题：走入极端一（晦涩工程手册腔），堆砌 IEEE 754 内存解释失真、操作系统段错误、词法中断、解耦重构等黑话，像工业级编译器架构文档；或走入极端二（做作幼稚学生腔），滥用第一人称并出现“问了同学”、“老老实实打逗号”、“黑框控制台”、“手抖输入了字母”等口语化做作表达，极度虚假。
   - 本项目解法：**黄金中庸之道（客观严谨的本科实验报告文风）**：弱化主观第一人称，采用客观陈述与实验观察视角（如“测试表明...”、“若未添加...导致...”、“修改为...后恢复正常”）；技术机理讲透但通俗直白（浮点与整型存储格式不同导致乱码、漏写取地址符引发非法内存访问崩溃、整除截断导致商为0）；务实求真，呈现优秀工科生水准的扎实报告质感。

---



## 仓库结构

```
hbu-c-programming-lab-skill/
├── SKILL.md                               # Skill 核心主规程与 SOP（大模型通用指令入口）
├── README.md                              # 仓库说明文档
├── LICENSE                                # 开源许可证 (MIT)
├── references/                            # 权威知识库与避坑参考指南
│   ├── guide_structure_and_checklist.md   # 指导书目录树与全量★题核查清单 (防漏写)
│   ├── tables_and_formatting_standards.md # 9大经典数据对比表格范式与OpenXML规范
│   └── avoiding_ai_traces.md              # 去AI味、严禁词汇表与真实学生人设规范
├── scripts/                               # 自动化质量检测与工具套件
│   └── validate_report.py                 # docx 实验报告全维度终检审查工具
└── resources/                             # 结构模板与配置文件样例
    └── sample_config.json                 # 学生基本信息与实验结构样例
```

---

## 自动化审查工具：validate_report.py

在报告提交前，使用配套的自动化脚本对生成的 `.docx` 文件执行全方位质量审查：

```bash
# 审查合并实验报告
python3 scripts/validate_report.py -f "/path/to/实验一至三合并报告张三20251234567.docx"

# 审查单次实验报告
python3 scripts/validate_report.py -f "/path/to/实验一张三20251234567.docx" --single
```

### 审查维度：
- **颜色合规性**：检测全文 `<w:color>` 标签数量，确保为 `0`（纯黑排版）。
- **违禁词与AI痕迹**：严查“契合”、“三大要求”、“Prompt”、“大模型”、“严格遵循六大步骤”等敏感说明书套话。
- **版面控制**：检查封面末尾空行与分页符，杜绝出现空白第 2 页。
- **表格数量**：验证外层大表格及内部数据对比表数量（保证表格化对比充分）。
- **附录代码完整性**：核验 7 个核心 C 源程序是否全量完整收录（无伪代码或省略号）。
- **★题覆盖率**：地毯式匹配指导书核心任务点，杜绝任何题目遗漏。



---

## 跨 AI Agent 生态配置与使用指引

本 Skill 设计为**全生态 AI Agent 通用规范**，可以在任意主流 AI 编码助手与 Agent 环境中无缝应用：

### 1. Antigravity CLI (agy) / Gemini CLI
克隆仓库后，在 `~/.gemini/config/skills/` 中建立软链接：
```bash
ln -s ~/workspace/hbu-c-programming-lab-skill ~/.gemini/config/skills/hbu-c-programming-lab-skill
```

### 2. Cursor
在你的工作区根目录下创建规则文件：
- 方式 A：将本仓库作为 submodule 或直接拷贝到 `.cursor/rules/hbu-c-lab.md`；
- 方式 B：在项目根目录 `.cursorrules` 中追加提示引用：
  ```
  编写河北大学电信学院C程序设计实验报告时，严格遵循 hbu-c-programming-lab-skill/SKILL.md 规范。
  ```

### 3. Cline / Roo-Code
在系统的 Custom Instructions 或项目 `.clinerules` 中载入：
```markdown
Refer to hbu-c-programming-lab-skill/SKILL.md for Hebei University C programming lab report generation standards.
```

### 4. Windsurf
在工作区 `.windsurfrules` 或 Cascade Settings 中将 `SKILL.md` 加入上下文规则。

### 5. Claude Desktop / ChatGPT / 网页端大模型
直接将 `SKILL.md` 及 `references/` 内容作为项目知识库（Project Knowledge）或系统提示词导入即可。

---

### 通用 Prompt 唤醒示例

配置完成后，向任意 AI Agent 发送类似以下提示：

> “使用 `hbu-c-programming-lab-skill` 规程，根据河北大学《C程序设计》实验指导书和电信学院模板，为我编写[实验一/实验一至三合并]报告。
> 姓名：张三，学号：20251234567，年级专业：2025级自动化。
> 严格执行：零漏写、结构1:1对齐、实验目的原句照搬、实验过程落实算法与核心代码、纯黑零色标、全表格化对比且无开篇套话废话。”

AI 将自动严格遵循规程，输出符合河大电信学院评阅标准的实验报告。

---

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
