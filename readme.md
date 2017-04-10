###gruntjs.com 爬取全站资源文件后在Django静态部署-使用说明
1.将爬取的资源文件放入templates中-html
2.将静态文件放入static文件夹中-包括css,fonts,img
3.修改对静态资源的引用路径：
>    打开replace.py 调用
 
 >change_css() 
 
 >change_img()
 
修正对资源文件的引用路径
4.生成views函数 和 url映射数组
>打开replace.py 调用
 
 >to_url()
 
将打印的数组元素复制到对应位置(例urls

>to_views()

将打印的view函数复制到对应位置(例views

5.启动服务检查网站


###gruntjs.com 爬取全站资源文件后在Django静态部署-编写思路-部署部分
>修改对静态资源的引用路径：
  在资源文件引用的url前面加上'/static/'路径      
     
     change_css()
     change_img()
     
>to_url() 生成映射

    读取目录下的html文件
    使用replace('_', '/')装换多层路径
    并调用views对应函数
    
>to_views() 生成界面函数

    读取读取目录下的html文件
    去掉所有非法字符生成函数名
    并返回对应的当前html文件