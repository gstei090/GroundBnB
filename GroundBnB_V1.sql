SET search_path = "GroundBnB";


CREATE TABLE Guest(
	GuestID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	firstName VARCHAR(30) NOT NULL,
	middleInitial VARCHAR(1),
	lastName VARCHAR(30) NOT NULL,
	--fullName VARCHAR(65) GENERATED ALWAYS AS (CONCAT_WS(' ', firstName, middleInitial, lastName)) stored,
	phoneNum INTEGER[] NOT NULL,
	email VARCHAR);

	
CREATE TABLE Host(
	HostID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	firstName VARCHAR(30) NOT NULL,
	middleInitial VARCHAR(1),
	lastName VARCHAR(30) NOT NULL,
	--fullName VARCHAR(61) AS (concat_ws(' ', firstName, middleInitial, lastName)),
	phoneNum INTEGER[] NOT NULL,
	email VARCHAR);

CREATE TABLE Payment(
	PaymentID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	SenderID INT,
	ReceiverID INT,
	TypeOfPayment VARCHAR CHECK ((TypeOfPayment = 'Chash') OR (TypeOfPayment = 'Credit') OR (TypeOfPayment = 'Check')),
	Amount Numeric(8,2),
	Satus VARCHAR CHECK ((Satus = 'Pending') OR (Satus = 'Sent') OR (Satus = 'Received')));
	
create table Address(
	AddressID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	HouseNumber integer not null,
	Street varchar(20) not null,
	City varchar(20) not null,
	Province varchar(20) not null,
	Country varchar(20) not null,
	PostalCode varchar(20) not null,
	primary key (AddressID));
	
create table Property (
	PropertyID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	AddressID INT not null,
	BuildingType varchar(20),
	RoomType varchar(20),
	Accomodates INT,
	Amenities varchar(20),
	Bathrooms integer,
	Availability varchar(20),
	Beds varchar(30)[],
	Price numeric(8,2),
	primary key (PropertyID),
	foreign key (AddressID) references Address,
	constraint checkBuilding check (BuildingType = 'house' OR BuildingType = 'apartment'),
	constraint checkRoom check(RoomType = 'single' OR RoomType = 'double'),
	constraint checkAccomodates check (Accomodates > 0),
	constraint checkBathrooms check (Bathrooms > 0),
	constraint checkAvailability check (Availability = 'available' OR Availability ='not available'));
	
CREATE TABLE RentalAgreement(
	RentalID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	HostID INT REFERENCES Host(HostID),
	PropertyID INT REFERENCES Property(PropertyID),
	SigningDate DATE,
	StartDate DATE,
	EndDate Date);
		
CREATE TABLE Booking(
	BookingID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	GuestID INT REFERENCES Guest(GuestID),
	StartDate DATE,
	EndDate DATE,
	NumGuests INT, -- CHECK (NumGuests <= Accomodates) WHERE (Property(PropertyID) =  ),
	PropertyID INT REFERENCES Property(PropertyID));
	

	
CREATE TABLE Reviews(
	ReviewID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	Rating INT CHECK ((Rating >= 0) OR (Rating <= 10)),
	Cleanliness INT CHECK ((Rating >= 0) OR (Rating <= 10)),
	ValueScore  INT CHECK ((Rating >= 0) OR (Rating <= 10)));
	
	

create table Employee (
	EmployeeID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	FirstName varchar (30) not null,
	MiddleInitial varchar(30),
	LastName varchar(30)not null,
	--FullName varchar (90) as (concat_ws(' ', FirstName, MiddleName, LastName)) not null,
	BranchID varchar(20) not null,
	SSN integer not null,
	Email varchar(40),
	Salary numeric(10,2) not null,
	PhoneNumber integer[] not null,
	EPosition varchar(20) DEFAULT 'Employee',
	primary key (EmployeeID),
	constraint checkSalary check (Salary > 0));
	
create table Branches(
	BranchID INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	Country varchar(30) not null,
	EmployeeID INT not null,
	primary key(BranchID),
	foreign key(EmployeeID) references Employee);
	
CREATE TABLE HasBooking(
	GuestID INT REFERENCES Guest(GuestID),
	BookingID INT REFERENCES Booking(BookingID) UNIQUE,
	PRIMARY KEY (GuestID, BookingID));
	
CREATE TABLE RegisteredAS(
	GuestID INT REFERENCES Guest(GuestID) UNIQUE,
	HostID INT REFERENCES Host(HostID) UNIQUE,
	PRIMARY KEY (GuestID, HostID ));
	
CREATE TABLE ReceivesPayment(
	HostID INT REFERENCES Host(HostID),
	PaymentID INT REFERENCES Payment(PaymentID) UNIQUE,
	PRIMARY KEY (HostID, PaymentID));
	
CREATE TABLE PayedFor(
	PaymentID INT REFERENCES Payment(PaymentID) UNIQUE,	
	BookingID INT REFERENCES Booking(BookingID) UNIQUE,
	PRIMARY KEY (PaymentID, BookingID));
	
CREATE TABLE SignedBy(
	HostID INT REFERENCES Host(HostID),
	RentalID INT REFERENCES RentalAgreement(RentalID) UNIQUE,
	PRIMARY KEY (HostID, RentalID));
	
CREATE TABLE LivesAt(
	HostID INT REFERENCES Host(HostID) UNIQUE,
	AddressID INT REFERENCES Address(AddressID),
	PRIMARY KEY (HostID, AddressID));
	
CREATE TABLE HasAgreement(
	RentalID INT REFERENCES RentalAgreement(RentalID),
	PropertyID INT REFERENCES Property(PropertyID) UNIQUE,
	PRIMARY KEY (RentalID, PropertyID));
	
CREATE TABLE BookedProperty(
	BookingID INT REFERENCES Booking(BookingID) UNIQUE,
	PropertyID INT REFERENCES Property(PropertyID),
	PRIMARY KEY (BookingID, PropertyID));
	
CREATE TABLE MakeReview(
	GuestID INT REFERENCES Guest(GuestID),
	ReviewID INT REFERENCES Reviews(ReviewId),
	PRIMARY KEY (GuestID, ReviewID));
	

CREATE TABLE HasReview(
	ReviewID INT REFERENCES Reviews(ReviewID),
	PropertyID INT REFERENCES Property(PropertyID),
	PRIMARY KEY (ReviewID, PropertyID));
	
create table HasAddress(
	AddressID INT not null,
	PropertyID INT not null unique,
	primary key(AddressID, PropertyID),
	foreign key(AddressID) references Address(AddressID),
	foreign key(PropertyID) references Property(PropertyID));

create table EmployeeLivesAt(
	EmployeeID INT not null unique,
	AddressID INT not null unique,
	primary key(AddressID, EmployeeID),
	foreign key(AddressID) references Address(AddressID),
	foreign key(EmployeeID) references Employee(EmployeeID));

create table WorksAt(
	BranchID INT not null,
	EmployeeID INT not null unique,
	primary key(BranchID, EmployeeID),
	foreign key(EmployeeID) references Employee(EmployeeID),
	foreign key(BranchID) references Branches(BranchID));

create table OperatingIn(
	BranchID INT not null,
	PropertyID INT not null unique,
	primary key(BranchID, PropertyID),
	foreign key(BranchID) references Branches(BranchID),
	foreign key(PropertyID) references Property(PropertyID));