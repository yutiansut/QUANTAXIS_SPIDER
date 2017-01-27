# 使用selenium-Mongodb搭建后台

爬虫思路:
> 首先进入登录页面,https://xueqiu.com/user/login,select 用户名框和密码框,勾选一直登录
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://xueqiu.com/user/login" />
<title>New Test</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">New Test</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>https://xueqiu.com/user/login</td>
	<td></td>
</tr>
<tr>
	<td>assertTitle</td>
	<td>登录 - 雪球</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>name=username</td>
	<td>13382753152</td>
</tr>
<tr>
	<td>type</td>
	<td>name=password</td>
	<td>Yutiansut940809</td>
</tr>
<tr>
	<td>click</td>
	<td>name=remember_me</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>css=button.button</td>
	<td></td>
</tr>
<tr>
	<td>assertTitle</td>
	<td>我的首页 - 雪球</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=pop_username</td>
	<td>13382753152</td>
</tr>
<tr>
	<td>type</td>
	<td>id=pop_password</td>
	<td>Yutiansut940809</td>
</tr>
<tr>
	<td>click</td>
	<td>id=head</td>
	<td></td>
</tr>

</tbody></table>
</body>
</html>
```