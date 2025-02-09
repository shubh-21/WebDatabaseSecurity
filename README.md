# Access Control Matrix (ACM)
It is a fundamental security model used in computer systems to define and manage access rights of subjects (users, processes) to objects (files, databases, resources).
- **Subjects**: Entities (users, processes) that request access.
- **Objects**: Resources (files, databases, devices) to be protected.
- **Operations**: Actions that subjects can perform on objects (e.g., read, write, execute).
- **Matrix Representation**: A table where:
  * **Rows** represent subjects.
  * **Columns** represent objects.
  * Each cell defines the **permissions** of a subject on an object.


### Scenario : 
Consider the scenario below: </br>
**Subjects** are as follows : </br>
1. Student
2. Teacher
3. Admin </br>

**Objects** are as follows : </br>
1. User Identification
2. Grading
3. Fee Payment
4. Course Enrollment </br>

**Rights** are as follows : </br>
1. Read
2. Write
3. Delete </br>

**Rights that Student hold over objects** :
- Student can Read User Identification database.
- Student can Read his/her Grades.
- Student can Read his/her Fee Payment Status.
- Student can Read and Write his/her Course Enrollment status.
  
**Rights that Teacher hold over objects** :
- Teacher can Read User Identification database.
- Teacher can Read and Write Grades.
- Teacher can Read Fee Payment Status.
- Teacher can Read Course Enrollment status.Rights that Admin hold over objects:-
- Admin can Read, Write and Delete in User Identification database.
- Admin can Read Grades.
- Admin can Read and Write Fee Payment Status.
- Admin can Read and Delete Course Enrollment status.
