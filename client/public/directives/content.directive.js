/**
 * Created by Nobay on 23/06/2017.
 */
retail.directive('content',function(){
        return{
            restrict:'E',
            transclude: true,
            replace: true,
            templateUrl : '/templates/content.template.html'
        }
    });