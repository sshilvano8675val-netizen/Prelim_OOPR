import java.util.Date;

public class HilvanoMidtermProj6 {

// Instance variables
private String studentNo;
private String studentName;
private Date dateOfBirth;
private Integer tariffPoints;

// Class variable
private static int noOfStudents = 0;

// Getters
public String getStudentNo() {
return studentNo;
}

public String getStudentName() {
return studentName;
}

public Date getDateOfBirth() {
return dateOfBirth;
}

public Integer getTariffPoints() {
return tariffPoints;
}

// Setters
public void setStudentNo(String studentNo) {
this.studentNo = studentNo;
}

public void setStudentName(String studentName) {
this.studentName = studentName;
}

public void setDateOfBirth(Date dateOfBirth) {
this.dateOfBirth = dateOfBirth;
}

public void setTariffPoints(Integer tariffPoints) {
if (tariffPoints >= 20 && tariffPoints <= 280) {
this.tariffPoints = tariffPoints;
} else {
throw new IllegalArgumentException(
"Tariff points must be between 20 and 280."
);
}
}

// First constructor - Default constructor
public HilvanoMidtermProj6() {
studentNo = "not known";
studentName = "not known";
dateOfBirth = new Date("01/01/1995");
tariffPoints = 20;

noOfStudents++;
}

// Second constructor - Parameterized constructor
public HilvanoMidtermProj6(String studentNo, String studentName,
Date dateOfBirth, Integer tariffPoints) {

this.studentNo = studentNo;
this.studentName = studentName;
this.dateOfBirth = dateOfBirth;
setTariffPoints(tariffPoints);

noOfStudents++;
}

// Getter for number of students
public static int getNoOfStudents() {
return noOfStudents;
}

// Main method - Part C
public static void main(String[] args) {

// Using the default constructor
HilvanoMidtermProj6 student1 = new HilvanoMidtermProj6();

// Using the parameterized constructor
HilvanoMidtermProj6 student2 = new HilvanoMidtermProj6(
"S001",
"John Smith",
new Date("15/06/2005"),
180
);

// Display information
System.out.println("Student 1: " + student1.getStudentName());
System.out.println("Student 2: " + student2.getStudentName());

System.out.println("Number of students: "
+ HilvanoMidtermProj6.getNoOfStudents());
}
}