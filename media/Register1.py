#!C:\Python310\python.exe
print("Content-type:text/html\n\r")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="Sugasuvi@123",database="BTSs")
cur=db.cursor()
print('''<style>
body{
 background-image:url('images3.jpg');
 background-repeat: No-repeat;
 background-attachment:fixed;
 background-size:cover;
}
</style>''')
print('''<style type='text/css'>
label{
 width:110px;
 display:inline-block;
 margin:15px;
 text-align: left;
}
body{
 text-align: center;
}

input[type=text],select{
 width:18%;
 padding:10px 20px;
 margin:8px 0;
 display:inline-block;
 border:1px solid #ccc;
 border-radius:4px;
 box-sizing:border-box;
}
</style>''')

print("<body>")
print("<center><h1> BTS Sports Accadamy</h1></center>")
print("<h2><center>Employee personal details </center></h2>")
print("<form action='info.py' method='post'>")
print('''<label>First Name:</label>
    <input type='text' name='fname' required><br>''')
print('''<label>Last name:</label>
      <input type='text' name='lname' required><br>''')
print('''<label>Date of Birth:</label>
      <input type='text' name='dob' required><br>''')
print('''<label>Age:</label>
      <input type='text' name='age' required><br>''')
print('''<label for="gen">Gender:</label>
        <select id="gen" name="gen">
        <option value="Select">Select</option>
	<option value="Male">Male</option>
        <option value="Female">Female</option>
    </select><br>''')
print('''<label>Joining Date:</label>
      <input type='text' name='jdate' required><br>''')
print('''<label>Mobil Number:</label>
      <input type='text' name='mn' required><br>''')
print('''<label>Address: </label>
      <input type='text' name='add'<br><br>''')
print('''<label for="Designation"><bold>Designation:</bold></label>
        <select id="" name="des">
        <option value="Select">Select</option>
	<option value="Vollyball">Vollyball</option>
        <option value="Throwball">Throwball</option>
        <option value="Badminton">Badminton</option>
        <option value="Cricket">Cricket</option>
        <option value="Skating">Skating</option>
    </select><br>''')
print("<input type='submit' Value='Register'>")
print("</form>")
print("<form action='regisde.py' method='post'>")
print("<center><input type='submit' Value='Exit'</center>")
print("</form>")















































        




        
        

