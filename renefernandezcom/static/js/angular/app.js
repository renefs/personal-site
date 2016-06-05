'use strict';

// Declare app level module which depends on views, and components
angular.module('personalApp', [
    'ngRoute',
    'personalApp.social'
]).config(['$locationProvider', '$routeProvider', function ($locationProvider, $routeProvider) {
    $locationProvider.hashPrefix('!');
}]);
