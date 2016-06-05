'use strict';

angular.module('personalApp.social', [
]).component('socialNetworks', {
    templateUrl: 'static/js/angular/components/social/social.html',
    controller: function PhoneListController() {
        this.description = "También puedes encontrarme en las redes sociales. Tengo una cuenta en casi todas las que existen, así que he tenido el detalle de poner a continuación solamente aquellas que creo que te pueden interesar más.",
        this.social_networks = [
            {
                name: 'Google+',
                link: 'https://plus.google.com/+ReneFernandezSanchez?rel=author',
                image: 'static/images/google-plus-logo.png'
            }, {
                name: 'Linkedin',
                link: 'http://es.linkedin.com/pub/ren%C3%A9-fern%C3%A1ndez-s%C3%A1nchez/26/702/738/',
                image: 'static/images/linkedin-logo.png'
            }, {
                name: 'Github',
                link: 'https://github.com/renefs87',
                image: 'static/images/github-logo.png'
            }, {
                name: 'Twitter',
                link: 'https://twitter.com/the_rocker',
                image: 'static/images/twitter-logo.png'
            }
        ];
    }
});
