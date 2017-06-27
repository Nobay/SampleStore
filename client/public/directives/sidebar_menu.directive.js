retail.directive('sidebarMenu', function(){
        return{
            transclude: true,
            replace: true,
            restrict:'E',
            templateUrl:'/templates/sidebar_menu.template.html'
        }
    });

retail.directive('sidebarMenuItem',function(){
        return{
            restrict:'E',
            scope:{
                title:'@itemTitle',
                link:'@itemLink',
                class:'@itemClass'
            },
            replace: true,
            template : '<li><a ui-sref="{{link}}" ><i class="{{class}}"></i> {{title}}</a></li>'
        }
    });
