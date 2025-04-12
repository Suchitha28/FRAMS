// var app = angular.module('EmployeeApp', ['ngRoute']);

// app.config(function($routeProvider) {
//     $routeProvider
//         .when('/', {
//             templateUrl: 'login.html',
//             controller: 'LoginController'
//         })
//         .when('/home', {
//             templateUrl: 'home.html',
//             controller: 'HomeController'
//         })
//         .when('/dashboard', {
//             templateUrl: 'dashboard.html',
//             controller: 'DashboardController'
//         })
//         .when('/employee', {
//             templateUrl: 'employee.html',
//             controller: 'EmployeeController'
//         })
//         .when('/register', {
//             templateUrl: 'register.html',
//             controller: 'RegisterController'
//         })
//         .otherwise({redirectTo: '/'});
// });

// app.controller('LoginController', function($scope, $location) {
//     $scope.login = function() {
//         if ($scope.username === 'admin' && $scope.password === 'admin123') {
//             $location.path('/home');
//         } else {
//             alert('Invalid credentials');
//         }
//     };
// });

// app.controller('HomeController', function($scope) {
//     $scope.message = "Welcome to the Employee Management System!";
// });

// // app.controller('LoginController', function($scope, $location) {
// //     $scope.login = function() {
// //         if ($scope.username === 'admin' && $scope.password === 'admin123') {
// //             localStorage.setItem('admin', JSON.stringify({ username: $scope.username }));
// //             $location.path('/home');
// //         } else {
// //             alert('Invalid credentials');
// //         }
// //     };
// // });

// // app.controller('HomeController', function($scope, $location) {
// //     let admin = JSON.parse(localStorage.getItem('admin'));
// //     if (!admin) {
// //         $location.path('/');
// //     }
// //     $scope.message = "Welcome to Employee Management!";
// // });


// app.controller('DashboardController', function($scope) {
//     $scope.message = "This is the dashboard.";
// });

// app.controller('EmployeeController', function($scope) {
//     $scope.message = "Employee list and details will be shown here.";
// });

// app.controller('RegisterController', function($scope) {
//     $scope.message = "Register new employees here.";
// });
  // 2nd code

// var app = angular.module('EmployeeApp', ['ngRoute']);

// app.config(function($routeProvider) {
//     $routeProvider
//         .when('/', {
//             templateUrl: 'login.html',
//             controller: 'LoginController'
//         })
//         .when('/home', {
//             templateUrl: 'home.html',
//             controller: 'HomeController'
//         })
//         .when('/dashboard', {
//             templateUrl: 'dashboard.html',
//             controller: 'DashboardController'
//         })
//         .when('/employee/:userid', {  // Dynamic employee details route
//             templateUrl: 'employee.html',
//             controller: 'EmployeeController'
//         })
//         .when('/register', {
//             templateUrl: 'register.html',
//             controller: 'RegisterController'
//         })
//         .otherwise({redirectTo: '/'});
// });

// // ✅ Login Controller
// app.controller('LoginController', function($scope, $location) {
//     $scope.login = function() {
//         if ($scope.username === 'admin' && $scope.password === 'admin123') {
//             $location.path('/home');
//         } else {
//             alert('Invalid credentials');
//         }
//     };
// });

// // ✅ Home Controller
// app.controller('HomeController', function($scope) {
//     $scope.message = "Welcome to the Employee Management System!";
// });

// // ✅ Dashboard Controller
// app.controller('DashboardController', function($scope, $location) {
//     $scope.users = [
//         { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/50" },
//         { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/50" },
//         { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/50" }
//     ];

//     $scope.viewEmployeeDetails = function(userid) {
//         $location.path('/employee/' + userid);  // Navigate to employee details page
//     };
// });

// // ✅ Employee Controller (Dynamic)
// app.controller('EmployeeController', function($scope, $routeParams) {
//     var userid = $routeParams.userid;

//     var employeeData = {
//         1: { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/100" },
//         2: { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/100" },
//         3: { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/100" }
//     };

//     $scope.user = employeeData[userid] || {};

//     $scope.attendanceRecords = [
//         { date: "2025-04-01", login: "09:00 AM", logout: "06:00 PM" },
//         { date: "2025-04-02", login: "09:15 AM", logout: "06:10 PM" }
//     ];
// });

// // ✅ Register Controller
// app.controller('RegisterController', function($scope) {
//     $scope.message = "Register new employees here.";
// });


// 3 code with all updates  DONT USE THIS CODE 

// var app = angular.module('EmployeeApp', ['ngRoute']);

// app.config(function($routeProvider) {
//     $routeProvider
//         .when('/', {
//             templateUrl: 'login.html',
//             controller: 'LoginController'
//         })
//         .when('/home', {
//             templateUrl: 'home.html',
//             controller: 'HomeController'
//         })
//         .when('/dashboard', {
//             templateUrl: 'dashboard.html',
//             controller: 'DashboardController'
//         })
//         .when('/employee', {
//             templateUrl: 'employee.html',
//             controller: 'EmployeeController'
//         })
//         .when('/employee/:userid', {  
//             templateUrl: 'employee-details.html',
//             controller: 'EmployeeDetailsController'
//         })
//         .when('/register', {
//             templateUrl: 'register.html',
//             controller: 'RegisterController'
//         })
//         .otherwise({redirectTo: '/'});
// });

// // ✅ Login Controller (Stores Session)
// app.controller('LoginController', function($scope, $location) {
//     $scope.login = function() {
//         if ($scope.username === 'admin' && $scope.password === 'admin123') {
//             localStorage.setItem("loggedIn", true);  
//             $location.path('/home');
//         } else {
//             alert('Invalid credentials');
//         }
//     };
// });

// // ✅ Home Controller (Handles Navigation)
// app.controller('HomeController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.goToDashboard = function() {
//         $location.path('/dashboard');
//     };
//     $scope.goToEmployee = function() {
//         $location.path('/employee');
//     };
//     $scope.goToRegister = function() {
//         $location.path('/register');
//     };
// });

// // ✅ Dashboard Controller (Shows Employees)
// app.controller('DashboardController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     function loadEmployees() {
//         let employees = JSON.parse(localStorage.getItem("employees")) || [];
//         $scope.users = employees;
//     }

//     loadEmployees();

//     $scope.viewEmployeeDetails = function(userid) {
//         $location.path('/employee/' + userid);
//     };
// });

// // ✅ Employee Controller (Lists All Employees)
// app.controller('EmployeeController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     function loadEmployees() {
//         let employees = JSON.parse(localStorage.getItem("employees")) || [];
//         $scope.users = employees;
//     }

//     loadEmployees();
// });

// // ✅ Employee Details Controller (Fetches Specific Employee)
// app.controller('EmployeeDetailsController', function($scope, $routeParams, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     var userid = $routeParams.userid;
//     let employees = JSON.parse(localStorage.getItem("employees")) || [];
//     $scope.user = employees.find(emp => emp.userid == userid) || {};

//     $scope.attendanceRecords = [
//         { date: "2025-04-01", login: "09:00 AM", logout: "06:00 PM" },
//         { date: "2025-04-02", login: "09:15 AM", logout: "06:10 PM" }
//     ];
// });

// // ✅ Register Controller (Saves Employees to localStorage)
// app.controller('RegisterController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.registerEmployee = function() {
//         let employees = JSON.parse(localStorage.getItem("employees")) || [];

//         let newEmployee = {
//             userid: employees.length + 1,
//             username: $scope.username,
//             email: $scope.email,
//             phone: $scope.phone,
//             photo: "https://via.placeholder.com/100"
//         };

//         employees.push(newEmployee);
//         localStorage.setItem("employees", JSON.stringify(employees));

//         alert("Employee Registered Successfully!");
//         $location.path('/dashboard');
//     };
// });




//  4TH CODE 

// var app = angular.module('EmployeeApp', ['ngRoute']);

// app.config(function($routeProvider) {
//     $routeProvider
//         .when('/', {
//             templateUrl: 'login.html',
//             controller: 'LoginController'
//         })
//         .when('/home', {
//             templateUrl: 'home.html',
//             controller: 'HomeController'
//         })
//         .when('/dashboard', {
//             templateUrl: 'dashboard.html',
//             controller: 'DashboardController'
//         })
//         .when('/employee/:userid', {
//             templateUrl: 'employee.html',
//             controller: 'EmployeeController'
//         })
//         .when('/register', {
//             templateUrl: 'register.html',
//             controller: 'RegisterController'
//         })
//         .otherwise({ redirectTo: '/' });
// });

// var isAuthenticated = false; // Simple authentication flag

// // ✅ Login Controller
// // app.controller('LoginController', function($scope, $location) {
// //     $scope.login = function() {
// //         if ($scope.username === 'Rahul' && $scope.password === 'Rahul123') {
// //             isAuthenticated = true;
// //             $location.path('/home');
// //         } else {
// //             alert('Invalid credentials');
// //         }
// //     };
// // });

// app.controller('LoginController', function($scope, $location) {
//     $scope.login = function() {
//         if ($scope.username === 'Rahul' && $scope.password === 'Rahul123') {
//             localStorage.setItem("loggedIn", true);
//             localStorage.setItem("adminName", $scope.username); // ✅ Store admin's name
//             $location.path('/home');
//         } else {
//             alert('Invalid credentials');
//         }
//     };
// });




// // ✅ Home Controller
// // app.controller('HomeController', function($scope, $location) {
// //     $scope.message = "Welcome to the Employee Management System!";
// // });

// app.controller('HomeController', function($scope, $location) {
//     $scope.message = "Welcome to the Employee Management System!";
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.adminName = localStorage.getItem("adminName") || "Admin"; // ✅ Fetch admin name

//     $scope.goToDashboard = function() {
//         $location.path('/dashboard');
//     };

//     $scope.goToRegister = function() {
//         $location.path('/register');
//     };
// });


// // ✅ Dashboard Controller
// app.controller('DashboardController', function($scope, $location) {
//     $scope.users = [
//         { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/50" },
//         { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/50" },
//         { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/50" }
//     ];

//     $scope.viewEmployeeDetails = function(userid) {
//         $location.path('/employee/' + userid);
//     };
// });

// // ✅ Employee Controller (Dynamic)
// app.controller('EmployeeController', function($scope, $routeParams) {
//     var userid = $routeParams.userid;
    
//     var employeeData = {
//         1: { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:00 AM", logout: "06:00 PM" },
//             { date: "2025-04-02", login: "09:15 AM", logout: "06:10 PM" }
//         ] },
//         2: { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:10 AM", logout: "06:20 PM" },
//             { date: "2025-04-02", login: "09:05 AM", logout: "06:15 PM" }
//         ] },
//         3: { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:30 AM", logout: "06:40 PM" },
//             { date: "2025-04-02", login: "09:00 AM", logout: "06:00 PM" }
//         ] }
//     };
    
//     $scope.user = employeeData[userid] || {};
//     $scope.attendanceRecords = $scope.user.attendance || [];
// });

// // ✅ Register Controller
// app.controller('RegisterController', function($scope) {
//     $scope.message = "Register new employees here.";
// });


// 5th slide modify code

// var app = angular.module('EmployeeApp', ['ngRoute']);

// app.config(function($routeProvider) {
//     $routeProvider
//         .when('/', {
//             templateUrl: 'login.html',
//             controller: 'LoginController'
//         })
//         .when('/home', {
//             templateUrl: 'home.html',
//             controller: 'HomeController'
//         })
//         .when('/dashboard', {
//             templateUrl: 'dashboard.html',
//             controller: 'DashboardController'
//         })
//         .when('/employee/:userid', {
//             templateUrl: 'employee.html',
//             controller: 'EmployeeController'
//         })
//         .when('/register', {
//             templateUrl: 'register.html',
//             controller: 'RegisterController'
//         })
//         .otherwise({ redirectTo: '/' });
// });

// // ✅ Login Controller
// app.controller('LoginController', function($scope, $location) {
//     $scope.login = function() {
//         if ($scope.username === 'Rahul' && $scope.password === 'Rahul123') {
//             localStorage.setItem("loggedIn", true);
//             localStorage.setItem("adminName", $scope.username); // ✅ Store admin name
//             $location.path('/home');
//         } else {
//             alert('Invalid credentials');
//         }
//     };
// });

// // ✅ Home Controller
// app.controller('HomeController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.message = "Welcome to the Employee Management System!";
//     $scope.adminName = localStorage.getItem("adminName") || "Admin"; // ✅ Fetch admin name

//     $scope.goToDashboard = function() {
//         $location.path('/dashboard');
//     };

//     $scope.goToRegister = function() {
//         $location.path('/register');
//     };

//     // ✅ Slideshow images
//     $scope.images = [
//         "images/image1.jpg",
//         "images/image2.jpg",
//         "images/image3.jpg",
//         "images/image4.jpg",
//         "images/image5.jpg",
//         "images/image6.jpg",
//         "images/image7.jpg",
//         "images/image8.jpg"
//     ];

//     // ✅ Initialize Swiper.js
//     setTimeout(function () {
//         var swiper = new Swiper(".swiper-container", {
//             loop: true,
//             autoplay: { delay: 2000 },
//             pagination: { el: ".swiper-pagination", clickable: true },
//             navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }
//         });
//     }, 500);
// });

// // ✅ Dashboard Controller
// app.controller('DashboardController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.users = [
//         { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/50" },
//         { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/50" },
//         { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/50" }
//     ];

//     $scope.viewEmployeeDetails = function(userid) {
//         $location.path('/employee/' + userid);
//     };
// });

// // ✅ Employee Controller (Dynamic)
// app.controller('EmployeeController', function($scope, $routeParams, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     var userid = $routeParams.userid;

//     var employeeData = {
//         1: { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:00 AM", logout: "06:00 PM" },
//             { date: "2025-04-02", login: "09:15 AM", logout: "06:10 PM" }
//         ] },
//         2: { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:10 AM", logout: "06:20 PM" },
//             { date: "2025-04-02", login: "09:05 AM", logout: "06:15 PM" }
//         ] },
//         3: { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212", photo: "https://via.placeholder.com/100", attendance: [
//             { date: "2025-04-01", login: "09:30 AM", logout: "06:40 PM" },
//             { date: "2025-04-02", login: "09:00 AM", logout: "06:00 PM" }
//         ] }
//     };

//     $scope.user = employeeData[userid] || {};
//     $scope.attendanceRecords = $scope.user.attendance || [];
// });

// // ✅ Register Controller
// app.controller('RegisterController', function($scope, $location) {
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }
    
//     $scope.message = "Register new employees here.";
// });










var app = angular.module('EmployeeApp', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'login.html',
            controller: 'LoginController'
        })
        .when('/home', {
            templateUrl: 'home.html',
            controller: 'HomeController'
        })
        .when('/dashboard', {
            templateUrl: 'dashboard.html',
            controller: 'DashboardController'
        })
        .when('/employee/:userid', {
            templateUrl: 'employee.html',
            controller: 'EmployeeController'
        })
        .when('/register', {
            templateUrl: 'register.html',
            controller: 'RegisterController'
        })
        .when('/admin_r', {
            templateUrl: 'admin_r.html',
            controller: 'AdminController'
        })
        .otherwise({ redirectTo: '/' });
});

// ✅ Login Controller
app.controller('LoginController', function($scope, $location) {
    $scope.login = function() {
        if ($scope.username === 'Rahul' && $scope.password === 'Rahul123') {
            localStorage.setItem("loggedIn", true);
            localStorage.setItem("adminName", $scope.username); // ✅ Store admin's name
            $location.path('/home');
        } else {
            alert('Invalid credentials');
        }
    };
});

// ✅ Home Controller (Now Includes Dynamic Image List)
// app.controller('HomeController', function($scope, $location) {
//     $scope.message = "Welcome to the Employee Management System!";
    
//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.adminName = localStorage.getItem("adminName") || "Admin"; // ✅ Fetch admin name

//     $scope.goToDashboard = function() {
//         $location.path('/dashboard');
//     };

//     $scope.goToRegister = function() {
//         $location.path('/register');
//     };

//     // ✅ Dynamic Image List for the Carousel
//     $scope.images = [
//         "images/photo1.jpg",
//         "images/photo2.jpg",
//         "images/photo3.jpg",
//         "images/photo4.jpg",
//         "images/photo5.jpg",
//         "images/photo6.jpg",
//         "images/photo7.jpg",
//         "images/photo8.jpg"
//     ];
// });

// var app = angular.module('employeeApp', []);

// app.controller('HomeController', function($scope, $window) {

//     $scope.goToDashboard = function() {
//         $window.location.href = "/dashboard";
//     };

//     $scope.goToRegister = function() {
//         $window.location.href = "/register";
//     };

//     $scope.goToAdmin = function() {
//         $window.location.href = "/admin_r";
//     };
    
// });
// var app = angular.module('employeeApp', []);

// app.controller('HomeController', function($scope, $window) {

//     $scope.goToDashboard = function() {
//         $window.location.href = "/dashboard";
//     };

//     $scope.goToRegister = function() {
//         $window.location.href = "/register";
//     };

//     $scope.goToAdmin = function() {
//         $window.location.href = "/admin_r";
//     };

// });

var app = angular.module('employeeApp', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
    .when('/dashboard', {
        templateUrl: 'dashboard.html',
        controller: 'DashboardController'
    })
    .when('/employee/:userid', {
        templateUrl: 'employee.html',
        controller: 'EmployeeController'
    })
    .otherwise({
        redirectTo: '/dashboard'
    });
});


// app.controller('HomeController', function($scope, $location) {
//     $scope.message = "Welcome to the Employee Management System!";

//     if (!localStorage.getItem("loggedIn")) {
//         $location.path('/');
//     }

//     $scope.adminName = localStorage.getItem("adminName") || "Admin";

//     $scope.goToDashboard = function() {
//         $location.path('/dashboard');
//     };

//     $scope.goToRegister = function() {
//         $location.path('/register');
//     };

//     $scope.goToAdmin = function() {
//         $location.path('/admin_r');
//     };


    // Ensure Bootstrap Carousel works
    setTimeout(function() {
        var myCarousel = new bootstrap.Carousel(document.querySelector('#photoCarousel'), {
            interval: 2000 // Faster slide changes (every 2 seconds)
        });
    }, 500);


// ✅ Dashboard Controller
// app.controller('DashboardController', function($scope, $location) {
//     $scope.users = [
//         { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210",  photo: "images/employees/rahul.jpeg" },
//         { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211",  photo: "images/employees/rahhhh.jpeg" },
//         { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212",  photo: "images/employees/suchh.jpeg"}
//     ];

//     $scope.viewEmployeeDetails = function(userid) {
//         $location.path('/employee/' + userid);
//     };
// });

app.controller('DashboardController', function($scope, $location) {
    $scope.users = [
        { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210",  photo: "images/employees/rahul.jpeg" },
        { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211",  photo: "images/employees/rahhhh.jpeg" },
        { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212",  photo: "images/employees/suchh.jpeg" }
    ];

    $scope.viewEmployeeDetails = function(userid) {
        $location.path('/employee/' + userid);
    };
  
});


// ✅ Employee Controller (Dynamic)
app.controller('EmployeeController', function($scope, $routeParams) {
    var userid = $routeParams.userid;
    
    var employeeData = {
        1: { userid: 1, username: "Rahul Gupta", email: "rahul@example.com", phone: "9876543210", photo: "images/employees/rahul.jpeg", attendance: [
            { date: "2025-04-01", login: "09:00 AM" },
            { date: "2025-04-02", login: "09:15 AM" }
        ] },
        2: { userid: 2, username: "John Doe", email: "john@example.com", phone: "9876543211", photo: "images/employees/rahhhh.jpeg", attendance: [
            { date: "2025-04-01", login: "09:10 AM" },
            { date: "2025-04-02", login: "09:05 AM" }
        ] },
        3: { userid: 3, username: "Jane Smith", email: "jane@example.com", phone: "9876543212",  photo: "images/employees/suchh.jpeg", attendance: [
            { date: "2025-04-01", login: "09:30 AM" },
            { date: "2025-04-02", login: "09:00 AM"}
        ] }
    };
    
    $scope.user = employeeData[userid] || {};
    $scope.attendanceRecords = $scope.user.attendance || [];
});

// ✅ Register Controller
app.controller('RegisterController', function($scope) {
    $scope.message = "Register new employees here.";
});

// ✅ Admin Controller
app.controller('AdminController', function($scope) {
    $scope.message = "Register new admin here.";
});
