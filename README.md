# botruntime — 多 RPA 作业依赖 DAG、异常重跑、断点续跑、凭据与并发、审计轨迹。

难度：**地狱**　|　子方向：数据采集 / 爬虫与 RPA　|　运行栈：Python 3.14 + 标准库 `sqlite3` + `httpx` + `pytest`（离线，无需联网）

## 基础版代码（起点，能跑）
读 `fixtures/input.json` → `loader` → `normalizer` → 其余已实现变换 → `keyer` → 幂等落 `sqlite`。
```
make run     # 跑通 happy-path，打印 {fed, rows}
make test    # happy-path + 幂等 + 缺口桩断言
```

## 单一职责约定
每个模块 = 一个文件 = 一个聚焦函数；`pipeline.py` 只做顺序编排、不含业务判断。
业务模块：`dag, scheduler, recovery, credential, concurrency, audit` ＋ 通用 `loader / normalizer / keyer / store / pipeline / cli`。

## 故意留空（功能开发面）
- `dag.py` → `process()` 抛 `NotImplementedError`（对记录做单一职责变换：dag；功能开发目标，未接入 happy-path）
- `recovery.py` → `process()` 抛 `NotImplementedError`（对记录做单一职责变换：recovery；功能开发目标，未接入 happy-path）

## 朴素实现短板（功能优化面）
- `scheduler.py` → 朴素实现 + docstring 标注短板（对记录做单一职责变换：scheduler；功能优化目标）
- `credential.py` → 朴素实现 + docstring 标注短板（对记录做单一职责变换：credential；功能优化目标）

> 缺口模块刻意未接入 happy-path，以保证基线可运行；它们正是出题要补的 0→1 / 1→n 功能。
