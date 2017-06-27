/**
 * Created by Nobay on 26/06/2017.
 */
retail.directive('formContent',function(){
        return{
            restrict:'E',
            transclude: true,
            replace: true,
            templateUrl : '/templates/form.template.html'
        }
    });