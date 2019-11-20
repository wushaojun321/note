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

  下面的优先级最高

  