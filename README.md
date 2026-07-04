# Research Action Guide

Research Action Guide is a Codex skill for turning literature evidence into an executable research-design plan.

It is designed for biomedical and life-science research projects where the goal is not merely to summarize papers, but to decide what to do next: which public datasets to screen, what to include or exclude, how to perform QC and integration, how to define cell identity or biological objects, which downstream analyses are justified, what validation is needed, and what technical roadmap should guide the project.

This skill was developed from single-cell, pan-cancer, tumor-immunology, spatial-transcriptomics, and public-data workflow reading, but the core pattern is broader: author choices are treated as evidence. A paper is useful not because it used a popular tool, but because it shows how researchers chose data, quality control, annotation, modeling, validation, and interpretation under a specific scientific pressure.

## What This Skill Produces

| Artifact | Purpose |
|---|---|
| Literature Corpus Protocol | Defines how papers are searched, screened, enriched, included, excluded, and stopped at saturation. |
| Paper Decision Audit | Analyzes one paper by asking why the authors made each major data, QC, integration, annotation, downstream-analysis, and validation choice. |
| Decision Matrix | Compresses audited papers into reusable decision logic for cross-paper comparison. |
| Cross-Paper Evidence Synthesis | Extracts higher-order rules from multiple papers and judges what the corpus can and cannot support. |
| Research Action Guide | Final project-level guide with dataset criteria, inclusion/exclusion rules, QC/integration/annotation strategy, downstream modules, validation logic, risks, literature support, and a technical roadmap. |

## What This Skill Is Not

- It is not a reference-manager workflow.
- It is not a paper-summary template.
- It is not a tool-name collection.
- It is not a generic literature review.
- It should not generate a final guide from weak or abstract-only evidence.

## Typical Use

Example request:

```text
I want to screen single-cell / pan-cancer / tumor-immunity / spatial-transcriptomics papers,
extract workflow-design principles,
and turn them into a Research Action Guide for my biological question:
"Does the spatial niche of mregDC determine immunotherapy response,
and is it functionally remodeled during tumor progression?"
```

The skill should then:

1. Treat the biological question as a synthesis lens.
2. Build or update a literature corpus.
3. Audit evidence-eligible papers at decision-node depth.
4. Build a Decision Matrix.
5. Synthesize cross-paper evidence.
6. Produce an actionable Research Action Guide.

## Installation

Clone or copy this repository into your Codex skills directory:

```bash
git clone https://github.com/baishuai001/Research-Action-Guide.git ~/.codex/skills/research-action-guide
```

On Windows, the target folder is usually:

```text
C:\Users\<your-user-name>\.codex\skills\research-action-guide
```

## Validation

Run:

```bash
python -m unittest discover -s tests
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
```

The final Research Action Guide can be checked with:

```bash
python scripts/check_research_action_guide.py --file ./research_action_guide/action_guides/research_action_guide.md
```

# 课题行动指南

Research Action Guide 是一个 Codex skill，用来把文献证据转化为可执行的研究设计方案。

它适用于生物医学和生命科学研究场景。它的目标不是简单总结文献，而是帮助研究者决定下一步应该怎么做：应该筛选哪些公共数据，哪些数据应该纳入或排除，如何做质控和整合，如何定义细胞身份或生物学对象，哪些下游分析有科学依据，哪些验证是必要的，以及整个课题应该采用怎样的技术路线。

这个 skill 起源于单细胞、泛癌、肿瘤免疫、空间转录组和公共数据分析类文献的 workflow 阅读，但它的核心思想更通用：把作者的“选择”当作证据来理解。一篇文章的价值不在于它用了某个流行工具，而在于它展示了研究者在特定科学压力下，如何选择数据、质控、注释、建模、验证和解释路径。

## 这个 Skill 会生成什么

| 产物 | 作用 |
|---|---|
| Literature Corpus Protocol / 文献集合协议 | 规定如何检索、筛选、补全文献信息、纳入、排除，并判断何时达到阶段性饱和。 |
| Paper Decision Audit / 单篇文献决策审计 | 分析单篇论文中作者为什么这样选择数据、质控、整合、注释、下游分析和验证方式。 |
| Decision Matrix / 决策矩阵 | 把多篇已审计文献压缩成可横向比较的研究设计逻辑。 |
| Cross-Paper Evidence Synthesis / 跨文献证据综合 | 从多篇文章中提取更高层次的研究设计规律，并判断当前文献集合能支持什么、不能支持什么。 |
| Research Action Guide / 课题行动指南 | 最终的项目级行动方案，包括数据筛选标准、纳入排除规则、质控/整合/注释策略、下游分析模块、验证逻辑、风险、文献支持和技术路线图。 |

## 这个 Skill 不是什么

- 不是文献管理器流程。
- 不是单篇文献摘要模板。
- 不是工具名称清单。
- 不是泛泛的综述写作模板。
- 不能用薄弱证据或只有摘要的文献直接生成最终行动指南。

## 典型使用方式

示例指令：

```text
我要筛选一批单细胞 / 泛癌 / 肿瘤免疫 / 空间转录组文献，
总结不同生物学问题对应的研究设计原则，
并最终形成一个课题行动指南。

我的生物学问题是：
mregDC 空间生态位是否决定肿瘤免疫治疗响应，
并在肿瘤进展中发生功能性重塑？
```

skill 应该依次完成：

1. 把生物学问题作为后续综合分析的视角。
2. 建立或更新文献集合。
3. 对证据充分的文献进行决策节点级别的单篇审计。
4. 建立 Decision Matrix。
5. 进行跨文献证据综合。
6. 生成可执行的 Research Action Guide / 课题行动指南。

## 安装方式

将本仓库克隆或复制到 Codex skills 目录：

```bash
git clone https://github.com/baishuai001/Research-Action-Guide.git ~/.codex/skills/research-action-guide
```

Windows 上通常是：

```text
C:\Users\<你的用户名>\.codex\skills\research-action-guide
```

## 验证方式

运行：

```bash
python -m unittest discover -s tests
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
```

最终生成的课题行动指南可用以下命令检查：

```bash
python scripts/check_research_action_guide.py --file ./research_action_guide/action_guides/research_action_guide.md
```
