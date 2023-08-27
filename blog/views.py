from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "volleyball1.jpg",
        "author": "Maya",
        "date": date(2023, 8, 12),
        "title": "What gives me energy?",
        "excerpt": "Every person should have something that gives them a certain motivation, relaxation, something that makes them go crazy and can't imagine their life without it. ",
        "content": """
          If someone asks me what it is - definitely sport! I really live by it, and I'm happy to every of my achievements, although it is not without failures... 
            
          When I was 13, I chose volleyball, 7 years have passed and I still enjoy it as much as the first time!
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "cooking.jpg",
        "author": "Maya",
        "date": date(2022, 8, 16),
        "title": "The best cinnabones in my life!",
        "excerpt": "Finally, I found a recipe for perfect cinnabons, which you can cook yourself, and they will definitely be better than in a cafe!",
        "content": """
          Dough:

1 cup warm milk (110 degrees F/45 degrees C)

2 eggs, room temperature

⅓ cup margarine, melted

4 ½ cups bread flour

1 teaspoon salt

½ cup white sugar

2 ½ teaspoons bread machine yeast

Filling:

1 cup brown sugar, packed

2 ½ tablespoons ground cinnamon

⅓ cup butter, softened

Icing:

1 ½ cups confectioners' sugar

¼ cup butter, softened

1 (3 ounce) package cream cheese, softened

½ teaspoon vanilla extract

⅛ teaspoon salt


Prepare dough: Place milk, eggs, margarine, flour, salt, white sugar, and yeast in the pan of a bread machine in the order recommended by the manufacturer. Select dough cycle; press Start.

When dough has doubled in size, turn it out onto a lightly floured surface. Cover it with a kitchen towel or plastic wrap and let it rest for 10 minutes.

Roll dough on a lightly floured surface to a 16x21-inch rectangle.

Prepare filling: Combine brown sugar and cinnamon in a small bowl. Spread softened butter over the dough, then sprinkle cinnamon-sugar mixture evenly over top.

Starting at the longer end, roll up the dough; cut into 12 rolls. Place rolls in a lightly greased 9x13-inch baking pan. Cover and let rise until nearly doubled, about 30 minutes.

Meanwhile, preheat the oven to 400 degrees F (200 degrees C).

Bake rolls in the preheated oven until golden brown, about 15 minutes.

While rolls are baking, prepare icing: Beat confectioners' sugar, butter, cream cheese, confectioners' sugar, vanilla, and salt until creamy.

Spread icing on warm rolls before serving.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "koln.jpg",
        "author": "Maya",
        "date": date(2023, 8, 27),
        "title": "Koln",
        "excerpt": "A place where I advise you to go if you are in Germany!",
        "content": """
          I am currently in Germany and I am trying to see as much as I can while I have the chance. 
          
          I went to Cologne at the weekend, and it's just incredible!! I had no idea that the building was so big!
           
          I really liked the Gothic style, and I advise everyone who will be here to come here
        """
    }
]
def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })