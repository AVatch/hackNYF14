$(document).ready(function() {

			var focus_level = 0;
			var focus_change = 0;
			var art = [];
			var artwork_index = 0;
			var user_id = 0;

			$("#artist").hide();
			$("#art_title").hide();
			$("#artist_bio").hide();
			$("#artist_pic_url").hide();
			$("#article").hide();

			$("#prompt").submit(function(e) {
				e.preventDefault();
				user_id = $("#user_id").val();
				$("#prompt").hide();
				grab_art();
			});

			$("#up").on('click', function(e) {
				focus_level++;
				focus_change = 1;
				console.log(focus_level.toString());
			});

			$("#down").on('click', function(e) {
				focus_level--;
				focus_change = -1;
				console.log(focus_level.toString());
			});

			function grab_art() {
				$.ajax({
					type: "GET",
					dataType: "json",
					url: "http://104.131.69.12:8888/grabart",
					success: function(data) {
						art = data["art"];
						console.log(art);
						artwork_index = 0;
						focus_level = 1;
						initialize_dom();
					},
				})
			};

			function initialize_dom() {
				console.log("Init Dom");
				$("#art_pic_url").attr('src', art[artwork_index]["art_pic_url"]);
				$("#art_pic_url").fadeIn("slow");
				$("#artist").html(art[artwork_index]["artist"]);
				$("#artist").hide();

				$("#art_title").html(art[artwork_index]["art_title"]);
				$("#art_title").hide();

				$("#artist_bio").html(art[artwork_index]["artist_bio"].substring(0,350));
				$("#artist_bio").hide();

				$("#artist_pic_url").attr('src', art[artwork_index]["artist_pic_url"]);
				$("#artist_pic_url").hide();
				refresh_focus();
				console.log("towards the end of the initialize loop");
			};

			function refresh_focus() {
				$.ajax({
					type: "GET",
					dataType: "json",
					url: "http://104.131.69.12:8888/pull/brain/" + user_id.toString(),
					success: function(data) {
						console.log("refresh focus - success loop");
						focus_change = data.focus_level - focus_level;
						focus_level = data.focus_level;
						update_dom();
					},
					complete: function() {
						setTimeout(refresh_focus, 5000);
					},
				});
				update_dom();
			};

			function fade_out() {
				$("#artist").fadeOut('slow');
				$("#art_title").hide('slow');
				$("#artist_bio").hide('slow');
				$("#artist_pic_url").hide('slow');
				$("#article").hide('slow');
			};

			function update_dom() {
				console.log("in the update dom method");
				if (focus_change >= 1) {
					if (focus_level == 2) {
						console.log("in update dom - case 2");
						$('#artist').fadeIn('slow');
						$('#art_title').fadeIn('slow');
					}
					if (focus_level == 3) {
						console.log("in update dom - case 3");
						$('#artist_bio').fadeIn('slow');
						$('#artist_pic_url').fadeIn('slow');
					}
					if (focus_level == 4) {
						console.log("in update dom - case 4");
						$('#article').fadeIn('slow');
					}
				} if (focus_change < 0){
					++artwork_index;
					focus_level = 0;
					fade_out();
					initialize_dom();
				}
			};	
});