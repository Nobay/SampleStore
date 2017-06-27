'use strict';
if(!localStorage.getItem("user_token"))
{
    localStorage.setItem("user_token", "");
}
var retail = angular.module("retail", ['ngResource']);

angular.module('app', [
        'retail',
        'app.routes'
    ]);
