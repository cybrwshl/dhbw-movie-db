var movieDbControllers = angular.module('movieDbControllers', []);

movieDbControllers.controller('MovieListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('file:///C:/Users/cybrwushl93/git/dhbw-movie-db/frontend/js/movies.json').success(function(data) {
      $scope.movies = data;
  });
}]);

movieDbControllers.controller('MovieDetailCtrl', ['$scope', '$routeParams', '$http',
  function ($scope, $routeParams, $http) {
    $http.get('file:///C:/Users/cybrwushl93/git/dhbw-movie-db/frontend/js/movie_' + $routeParams.movieId + '.json').success(function(data) {
      $scope.movie = data;
  });
}]);

movieDbControllers.controller('PersonListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('file:///C:/Users/cybrwushl93/git/dhbw-movie-db/frontend/js/person.json').success(function(data) {
      $scope.persons = data;
  });
}]);

movieDbControllers.controller('PersonDetailCtrl', ['$scope', '$routeParams', '$http',
  function ($scope, $routeParams, $http) {
    $http.get('file:///C:/Users/cybrwushl93/git/dhbw-movie-db/frontend/js/person_' + $routeParams.personId + '.json').success(function(data) {
      $scope.person = data;
  });
}]);