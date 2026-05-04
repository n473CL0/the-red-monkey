# Deploy to GitHub Pages

## Quick Setup

### 1. Create GitHub Repository
- Go to [github.com](https://github.com) and create a new repository
- Name it whatever you like (e.g., `red-monkey-pub`)
- Don't initialize with README (you already have files)

### 2. Push Your Code to GitHub
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Red Monkey pub site"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

### 4. Update _config.yml
Update your `_config.yml` with your GitHub Pages URL:

```yaml
url: "https://YOUR-USERNAME.github.io"
baseurl: "/YOUR-REPO-NAME"
```

If using a custom domain or username.github.io repo:
```yaml
url: "https://YOUR-USERNAME.github.io"
baseurl: ""
```

### 5. Push the Config Update
```bash
git add _config.yml
git commit -m "Update config for GitHub Pages"
git push
```

### 6. Wait for Deployment
- GitHub will automatically build and deploy your site
- Check the **Actions** tab to see build progress
- Your site will be live at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME`
- Usually takes 1-3 minutes

## Custom Domain (Optional)

If you want to use your own domain (e.g., theredmonkey.pub):

1. Create a file named `CNAME` in your repository root:
   ```
   theredmonkey.pub
   ```

2. Update `_config.yml`:
   ```yaml
   url: "https://theredmonkey.pub"
   baseurl: ""
   ```

3. Configure DNS with your domain provider:
   - Add A records pointing to GitHub's IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - Or add a CNAME record pointing to: `YOUR-USERNAME.github.io`

4. In GitHub Settings > Pages, enter your custom domain and save

## Troubleshooting

**Site not loading?**
- Check the Actions tab for build errors
- Verify `_config.yml` has correct `url` and `baseurl`
- Make sure GitHub Pages is enabled in Settings

**CSS/Images not loading?**
- Check that `baseurl` is set correctly in `_config.yml`
- All asset links should use `{{ "/assets/..." | relative_url }}`

**Build failing?**
- Check the Actions tab for error details
- Common issue: missing `Gemfile` or `Gemfile.lock`
- GitHub Pages uses specific Jekyll versions - check compatibility

## Local Testing Before Deploy

Test your site locally with the GitHub Pages environment:

```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# View at http://localhost:4000
```
