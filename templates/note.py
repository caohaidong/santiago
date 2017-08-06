"""
# static readme

定制admin模板
我们下面将看到，你有几种工具来定制内建的admin模板，但是对于其它任务，例如需要自定义工作流或者细粒度权限
你将需要阅读本章末尾讲到的定制admin视图
现在我们来看看快速定制admin的外观和行为，第6章讲到了一些常见的任务，如更改logo样式和提供自定义admin表单
就这点来说，我们通常需要更改一个特殊项的一些模板
admin的每一个视图，如更改列表，编辑表单，删除确认页面，历史视图等都有一个分配的模板
而这个模板可以通过几种方式来覆盖
首先，你可以全局覆盖模板，admin视图使用标准模板载入机制来寻找模板，所以如果你在你的模板目录里创建模板
Django将载入并使用这些模板而不是使用Django绑定的默认admin模板
这些全局模板如下:
视图 基本模板名
更改列表 admin/change_list.html
增加/编辑表单 admin/change_form.html
删除确认 admin/delete_confirmation.html
对象历史 admin/object_history.html
尽管如此，大多数情况下你只想更改一个单独的对象或者app的模板而不是全局的模板
这样的话，每个admin视图首先寻找模型和app专有的模板，这些视图按下面的顺序寻找模板:
admin/<app_lable>/<object_name>/<template>.html
admin/<app_lable>/<template>.html
admin/<template>.html
例如，在bookstore app的Book模型的增加/编辑表单的视图(第6章的例子)按下面的顺序寻找模板:
admin/bookstore/book/change_form.html
admin/bookstore/change_form.html
admin/change_form.html

"""