'use strict';

angular.module('tempAngularApp')
    .controller('MainCtrl', function($scope, $resource, $log, $http) {
        $scope.awesomeThings = [
            'HTML5 Boilerplate',
            'AngularJS',
            'Karma'
        ];
        var Contact = $resource('/api/:version/contacts/:id', {
            version: 'v1',
            id: '@id'
        });
        $scope.fetch_contacts = function() {
            var contacts = Contact.query(function() {
                $log.info(contacts);
            });
        };
        $scope.add_contact = function() {
            var newContact = new Contact({
                'name': 'Vamshi',
                'phone': '1001001001',
                'email': 'vamshi@example.com'
            });
            newContact.name = 'Vamshi Krishna';
            newContact.$save();
        };
        $http.get('todos.json')
            .then(function(res) {
                $scope.todos = res.data;
            });
    });
