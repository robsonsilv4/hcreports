(function () {
  'use strict';
  angular
    .module('app')
    .controller('ReportController', function ($scope, $rootScope, $http) {
      $scope.showModal = false;
      $scope.reportResponses = [];

      $scope.toggleModal = function (reportResponses) {
        console.log(reportResponses);
        $scope.reportResponses = reportResponses;
        $scope.showModal = !$scope.showModal;
      };

      $http.get(`${$rootScope.baseUrl}/reports/`).then(function (response) {
        const reports = response.data.results;
        $scope.reports = reports;
      });
    });
})();
