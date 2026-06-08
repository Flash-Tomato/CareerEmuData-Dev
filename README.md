# 【华为openJiuwen】职场长程生存与晋升挑战（CCF BDCI 2026）赛题数据

[![Documentation](https://img.shields.io/badge/赛题文档-blue?style=for-the-badge&logo=readthedocs&link=https%3A%2F%2Fcareer-emulator.readthedocs.io%2Fen%2Flatest%2Findex.html)](https://career-emulator.readthedocs.io) [![GitCode Dev](https://img.shields.io/badge/%E5%8F%82%E8%B5%9B%E7%94%A8GitCode%E4%BB%93-brown?style=for-the-badge&logo=GitCode)](https://gitcode.com/SushiNinja/CareerSim-BDCI26) [![GitHub Dev](https://img.shields.io/badge/%E5%8F%82%E8%B5%9B%E7%94%A8GitHub%E4%BB%93-black?style=for-the-badge&logo=GitHub)](https://github.com/Trenza1ore/CareerSim-BDCI26)

`career-emulator-bdci26` 为 [career-emulator](https://pypi.org/p/career-emulator) 模拟器提供比赛所需的事件与配置数据，方便参赛选手通过 PyPI 直接获取题库。

## 安装

```bash
pip install "career-emulator[bdci26]"
```

## 使用

安装 `career-emulator-bdci26` 后，在 `career-emulator` 中以分发模式加载数据即可：

```bash
career-emulator update --source distribution --split dev
```

或在代码中：

```python
from career_emulator.storage import update_dataset

update_dataset(source="distribution")
```

若没有传入 ` --split`，`career-emulator` 会根据环境变量 `CAREER_EMULATOR_DATASET`（默认 `dev`）自动选择对应的集合。

## 相关链接

- 赛事入口：<https://www.xir.cn/competition/races/BDCI2026>
- 赛题文档：<https://career-emulator.readthedocs.io>
- 源码仓库：<https://github.com/Trenza1ore/CareerSim-BDCI26>
- GitCode：<https://gitcode.com/SushiNinja/CareerSim-BDCI26>
