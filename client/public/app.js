'use strict';

var retail = angular.module("retail", ['ngResource']);

angular.module('app', [
        'retail',
        'app.routes'
    ]);
