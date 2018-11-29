# 快速使用
## 安装 android ide
> [下载地址](https://developer.android.google.cn/studio/index.html)

## gradle 配置修改

'''
allprojects {
    repositories {
        def REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public/'
        all { ArtifactRepository repo ->
            if(repo instanceof MavenArtifactRepository){
                def url = repo.url.toString()
                if (url.startsWith('https://repo1.maven.org/maven2') || url.startsWith('https://jcenter.bintray.com/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $REPOSITORY_URL."
                    remove repo
                }
            }
        }
        maven {
            url REPOSITORY_URL
        }
    }
}

'''

## 安装 appium server
> [下载地址](https://github.com/appium/appium-desktop/releases/tag/v1.8.2)

> [Sample Code](https://github.com/appium/appium/tree/master/sample-code)

##### 生成 requirements.txt
> pip freeze > requirements.txt

##### 倒入依赖 requirements.txt
> pip install -r requirements.txt

