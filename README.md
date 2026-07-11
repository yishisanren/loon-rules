# loon-rules

> ⚠️ **本仓库已整合进 [`proxy-rulesets`](https://github.com/yishisanren/proxy-rulesets)（统一规则集仓库）。**
> 本仓库仍保留、旧订阅地址继续可用，但**不再更新**。新订阅请用：
> - Loon 原生：`…/proxy-rulesets/main/broker/broker-hk.list`
> - NekoBox/sing-box：`…/proxy-rulesets/main/broker/broker-hk.srs`（或 `.json`）
> 完整地址表见新仓库 README。

个人维护的 Loon 远程规则集。

## broker-hk.list

富途 + 老虎证券域名,用于「香港时延优选」分流。

**订阅链接:**

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/broker-hk.list
```

**Loon 引用方式**(`[Remote Rule]` 段):

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/broker-hk.list, policy=香港时延优选, tag=券商, enabled=true
```

## sing-box / homeproxy / NekoBox 订阅

`.list` 改动后,GitHub Actions 会自动把它转换成 sing-box 规则集,输出到 `srs/`
(由 `scripts/loon2singbox.py` 生成,请勿手改 `srs/` 下的文件)。每个 `*.list` 会生成:

- `srs/<name>.json` — sing-box **source** 源码格式(version 1)
- `srs/<name>.srs` — 编译后的 **binary** 规则集(SRS binary v1)

> 为什么是 version 1 / SRS v1:NekoBox / NekoRay 内置的 sing-box core 通常偏旧,
> 只吃 v1;新版 v2/v3 会加载失败。v1 对本仓库这类 domain/domain_suffix 规则完全够用,
> 且当前 sing-box 也照常识别,兼容性最广。

### NekoBox / NekoRay

**二进制版(推荐)** — 路由 → 规则集 → 添加,类型 `Remote`、格式 `Binary`:

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/srs/broker-hk.srs
```

**源码版(最保险,任何 core 版本都吃)** — 格式选 `Source`:

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/srs/broker-hk.json
```

规则集匹配后,出站/策略指向你的**香港节点**(这是分流规则,不是拦截)。

### homeproxy

「规则集」远程订阅(类型 `remote`,格式 `source`):

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/srs/broker-hk.json
```

新增 `.list` 时无需额外配置,工作流会自动为每个 `*.list` 生成同名 `srs/<name>.json` 和 `srs/<name>.srs`。
