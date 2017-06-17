console.log("test test")
var app = angular.module("app.directives",[]);
    app.directive('mySidebarMenu', function(){
        return{
            transclude: true,
            replace: true,
            restrict:'E',
            templateUrl:'static/directives/my_sidebar_menu.html',
            controller : function($scope){
                this.addItem = function(val){
                    console.log(val);
                }
            }
        }
    });

    app.directive('mySidebarMenuItem',function(){
        return{
            restrict:'E',
            scope:{
                title:'@myTitle',
                link:'@myLink',
                class:'@myClass'
            },
            replace: true,
            template : '<li><a href="{{link}}"><i class="{{class}}"></i> {{title}}</a></li>'
        }
    });

    app.directive('myContent',function(){
        return{
            restrict:'E',
            transclude: true,
            replace: true,
            templateUrl : 'static/directives/my_content.html'
        }
    });