# Post Hero Image Skill

## 目标

为 Computing Life 的一篇文章生成一对 light/dark 抽象题图。题图用于小尺寸入口识别，通常显示在 128×128 到 256×256，不是文章内插图、封面海报或标题复述。

## 适用场景

当需要给单篇博客文章或一组文章生成主题图、hero thumbnail、social preview concept image 时使用本 skill。

不要用本 skill 生成正文解释图、数据图、产品截图、文章配图或 News 站 `/share/` 的图片。这里的目标是主博客文章的抽象情绪索引。

当前主博客题图路线处于 deprioritized 状态。设计判断见 `docs/deprioritized_post_image.md`。除非明确重新启动这条路线，否则不要把生成结果接入模板、frontmatter 或正式图片目录。

## 验收标准

一组题图生成完成时，必须满足这些条件：

1. 每篇文章有一张 light 图和一张 dark 图。
2. dark 图必须由对应 light 图作为输入 edit/recolor 得到，不能用独立 text-to-image prompt 重新抽样。
3. light/dark 两张图的构图、silhouette、元素数量、几何关系和 visual metaphor 基本一致，只改变配色。
4. 图片缩到 128×128 时仍能留下清楚主题情绪；如果只能在大图里看懂，就不合格。
5. 视觉风格是 flat、简约、抽象、克制；不得出现 gradient、glow、neon、poster style、赛博背景、人物、机器人、文字、logo 或字面图标。
6. 产物落到临时或明确目标目录；实验产物默认不进 Git。

## 固定 Palette

生成 prompt 必须显式指定 palette，避免 GPT-Image-2 漂到随机美术风格。

Light：

| 用途 | 颜色 |
|---|---|
| 背景 | `#F8F9FB` |
| 主形状 | `#2547E0` |
| 次级形状 | `#A9B2C3` |
| 暖色点缀 | `#D99A24` |
| 小面积高亮 | `#FFF2C2` |

Dark：

| 用途 | 颜色 |
|---|---|
| 背景 | `#0D0F14` |
| 主形状 | `#8EA2FF` |
| 次级形状 | `#394256` |
| 暖色点缀 | `#D99A24` |
| 小面积高亮 | `#FFF2C2` |

## 生成策略

用 GPT-Image-2。先生成 light，再用 light 作为输入生成 dark。

Light prompt 的重点是文章主题、核心 visual motif、固定 palette、小尺寸约束和禁止项。不要要求模型解释文章；只要求它在小图里表达主题情绪。

Dark prompt 的重点是“只换色，不重画”。必须明确要求 preserve exact composition、silhouette、layout、object count、proportions、edge geometry、visual metaphor。dark 图如果看起来像另一张新图，应该重做。

通用 image generation CLI 见 workspace skill：`rules/skills/generate_image.md`。GPT-Image-2 多图生成应并行，单任务 timeout 至少 420 秒。

## Prompt 模板

Light：

```text
Create a square 1:1 abstract thumbnail for a technical personal blog. It will be displayed at 128x128 to 256x256 pixels, so it must be very simple, legible, and iconic.

Article: {title}
Theme: {theme}
Core motif: {one concise visual relationship, not keywords}
Palette: background #F8F9FB, main cobalt #2547E0, secondary slate #A9B2C3, accent muted amber #D99A24, tiny cream #FFF2C2 only if needed.

Style constraints: flat vector-like color blocks, solid fills only, no gradients, no glow, no neon, no shadows, no lens flare, no metallic reflection, no photorealistic lighting, no texture-heavy background, no poster style.
Content constraints: no text, no letters, no numbers, no people, no robots, no literal object icons, no browser logo, no medical symbol, no bed, no telescope, no generic AI brain.
Composition: one clear central silhouette, 3 to 6 shapes maximum, strong negative space, elegant and restrained, premium editorial icon, harmonious with a cobalt-blue engineering notebook website.
Goal: communicate mood and topic category in one glance, not explain the article.
```

Dark edit:

```text
Recolor this image into a dark-mode version for the same technical personal blog.

Preserve the exact composition, silhouette, layout, object count, proportions, edge geometry, and visual metaphor from the input image. Do not redesign it. Do not add or remove shapes. Only change the color scheme.

Target palette: background #0D0F14, main mist cobalt #8EA2FF, secondary deep slate #394256, accent muted amber #D99A24, tiny cream #FFF2C2 only if needed.

Keep the same flat vector-like solid-fill style. No gradients, no glow, no neon, no shadows, no lens flare, no photorealistic lighting. The dark version must look like the same icon with a different theme, not a new image.
```

## 输出建议

实验阶段放在 `docs/tmp_post_hero_images/` 这类 `tmp` 路径下，不进 Git。当前不要生成正式资源。未来如果重新启动，再放到 `content/images/heroes/`，并决定用 frontmatter 显式字段还是 slug-based manifest。

建议同时生成一个 128px contact sheet。审稿优先看 contact sheet，而不是看单张大图。题图实际用途是小尺寸扫描，不能被大图细节误导。

## 已知陷阱

独立生成 light/dark 会导致两张图构图不同。用户切换主题时会看到内容跳变，像换了一张文章图。正确做法是用 light 作为 input edit 出 dark。

SVG 路线在本轮实验里不作为主路线。它可控但容易显得硬，难以快速获得简约、典雅、高级的情绪。当前优先 GPT-Image-2 + 严格 palette + flat style。

Prompt 里只说 “minimal” 不够。模型仍然会加渐变、光效、赛博背景和海报构图。必须显式禁止 gradient、glow、neon、poster style、photorealistic lighting 和 texture-heavy background。
