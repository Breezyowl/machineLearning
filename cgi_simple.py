import cgi

path='/Users/zhangming/Desktop/simple.dat'

form=cgi.FieldStorage()

text=form.getvalue('text',open(path).read())
f=open(path,'w+')
f.write(text)
f.close()

print("""Content-Type: text/html; charset=utf-8
<html>
   <head>
      <title> simple editor</title>
   </head>
    <body>
      <form action ='simple_edit.sgi' method= 'POST'>
      <textarea rows='10' cols='20' name='text'>%s</textarea><br />
      <input type ='submit'/>
      </form>

    </body>
 </html>
"""% text


)
