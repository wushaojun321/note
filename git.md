## git lfs

安装

```bash
brew install git-lfs
git lfs install
```

使用

```bash
git lfs track captcha.png
git add .gitattributes
git commit -m "lfs test"
git push
```

遇到的问题

1. origin 不支持lfs

   ```
   git config lfs.https://github.com/wushaojun321/note.git/info/lfs.locksverify false
   ```

2. ssl 验证失败：certificate signed by unknown authority

   ```bash
   git config http.sslVerify false #关掉不验证
   ```


### git配置

- 命令行

  ```bash
  git config --system user.name # 对应/etc/gitconfig
  git config --global user.name # 对应~/.gitconfig
  git config user.name # 对应./.git/config
  ```

  从上到下，优先级越来越高

  



### git rm --cached

- 不删除文件，删除add，git将不再追踪它

### git rm

- git将删除文件和追踪

### git commit -amend -m "xxx"

- 提交到上一次的commit中，如果暂存区为空，会覆盖msg

### git diff --staged

- 只显示add之后的，也就是下一次commit提交的