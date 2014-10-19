$(document).ready(function() {

			var focus_level = 0;
			var artwork = [];
			var artwork_index = 0;
			var id = 0;

			$("#prompt").submit(function(e) {
				e.preventDefault();
				id = $("#user_id").val();
				console.log(id);
			});

});