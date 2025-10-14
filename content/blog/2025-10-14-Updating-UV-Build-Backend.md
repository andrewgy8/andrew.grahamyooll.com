---
title: Updating UV Build Backend
tags:
  - Python
  - Programming
---
On my hobby project [bakesite](https://github.com/andrewgy8/bakesite), I recently updated the build backend to use new default [uv_build](https://docs.astral.sh/uv/concepts/build-backend/#the-uv-build-backend) instead of the previous default hatchling. 

This is how it was done:

```
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -31,8 +31,8 @@ dependencies = [
 bakesite = "bakesite:main"
 
 [build-system]
-requires = ["hatchling"]
-build-backend = "hatchling.build"
+requires = ["uv_build>=0.9.2,<0.10.0"]
+build-backend = "uv_build"
```


Like most things with uv, stuff works out-of-the-box.
