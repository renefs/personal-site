'use strict';

// Declare app level module which depends on views, and components
angular.module('personalApp', [
    'ngRoute',
    'pascalprecht.translate',
    'ngSanitize',
    'personalApp.social'
]).config(['$translateProvider', '$locationProvider', '$routeProvider', function ($translateProvider, $locationProvider, $routeProvider) {
    $locationProvider.hashPrefix('!');

    $translateProvider.useSanitizeValueStrategy('sanitize');

    $translateProvider.translations('en', {
        'SOCIAL_LEAD': 'You can also find me on several social networks. I have an account in almost everyone! These are some of them.',
        'SOCIAL_TITLE': 'Social.'
    });

    $translateProvider.translations('es', {
        'SOCIAL_LEAD': 'También puedes encontrarme en las redes sociales. Tengo una cuenta en casi todas las que existen, así que he tenido el detalle de poner a continuación solamente aquellas que creo que te pueden interesar más.',
        'SOCIAL_TITLE': 'Social.'
    });
    $translateProvider.preferredLanguage('en');

}]);