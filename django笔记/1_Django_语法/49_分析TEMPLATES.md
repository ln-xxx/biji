

- settings.py

```
TEMPLATES = [
			    {
			        #渲染引擎
			        'BACKEND': 'django.template.backends.django.DjangoTemplates',
			        'DIRS': [os.path.join(BASE_DIR, 'templates')] # html模板存放的位置
			        ,
			        'APP_DIRS': True, 
			        # 当项目下的templates目录中找不到页面会继续到应用包下的templates目录中查找
			        'OPTIONS': {
			            'context_processors': [ # 全局上下文
			                'django.template.context_processors.debug',
			                'django.template.context_processors.request',
			                'django.contrib.auth.context_processors.auth',
			                'django.contrib.messages.context_processors.messages',
			            ],
			        },
			    },
			]
						


```