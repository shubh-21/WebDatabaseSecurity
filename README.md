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


## Access Control Table

| Subjects \ Objects  | User Identification | Grading | Fee Payment | Course Enroll |
|--------------------|-------------------|---------|------------|--------------|
| **Student**       | R                 | R       | R          | RW           |
| **Teacher**       | R                 | RW      | R          | R            |
| **Admin**         | RWD               | R       | RW         | RD           |

**Legend** :
- **R** = Read
- **W** = Write
- **D** = Delete


### Definition:
- **Capability List (C-List):** A list that stores the access rights of a specific subject (user/process) over various objects.
- **Access Control List (ACL):** A list that stores access rights of all subjects for a specific object.

### Capability List (Per Subject):
- **Student** → [User Identification (R), Grading (R), Fee Payment (R), Course Enroll (RW)]
- **Teacher** → [User Identification (R), Grading (RW), Fee Payment (R), Course Enroll (R)]
- **Admin** → [User Identification (RWD), Grading (R), Fee Payment (RW), Course Enroll (RD)]

### Access Control List (Per Object):
- **User Identification** → [Student (R), Teacher (R), Admin (RWD)]
- **Grading** → [Student (R), Teacher (RW), Admin (R)]
- **Fee Payment** → [Student (R), Teacher (R), Admin (RW)]
- **Course Enroll** → [Student (RW), Teacher (R), Admin (RD)]
