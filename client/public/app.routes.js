angular.module('app.routes',["ui.router"])
    .config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/login');

    $stateProvider
        .state('register', {
            url: '/register',
            templateUrl: '/templates/register.template.html',
            controller: 'CategoryController'
        })

        .state('authentication', {
            abstract: true,
            views:{
                'globalContent': {
                    template: '<form-content></form-content>'
                },
            }
         })

        .state('login', {
            parent: 'authentication',
            url: '/login',
            views:{
                'formContent': {
                    templateUrl: '/templates/login.template.html',
                    controller: 'LoginController',
                }
            }
        })

        .state('home', {
            abstract: true,
            views:{
                'globalContent': {
                    template: '<content></content>',
                }
            }
        })
        .state('home-content', {
            url: '/',
            parent: 'home',
            views:{
                'homeContent': {
                    templateUrl: '/templates/home.template.html',
                    controller: 'HomeController',
                }
            }
        })

        .state('categories', {
            parent: 'home',
            url: '/categories',
            views:{
                'homeContent': {
                    templateUrl: '/templates/categories.template.html',
                    controller: 'CategoryController',
                }
            }

        });

});

