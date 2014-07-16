'use strict';

angular.module('tempAngularApp')
  .controller('MainCtrl', function ($scope,$http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $http.get('/api/v1/contacts').success(function(data){
        console.log(data);
    });
  });
