from flask import Flask, render_template

app = Flask(__name__)

SOCIAL_LINKS = {
    "github": "https://github.com/aaronjsmith4328",
    "linkedin": "#",  # TODO: replace with real LinkedIn URL
    "blog": "https://asmithblogs.bearblog.dev/",
}

PROJECTS = [
    {
        "name": "PumpkynSPICE",
        "description": "Toy SPICE simulator written in Python",
        "url": "https://github.com/aaronjsmith4328/PumpkynSPICE",
    },
    {
        "name": "Rystretto",
        "description": "Toy logic synthesis tool built for learning",
        "url": "https://github.com/aaronjsmith4328/Rystretto",
    },
    {
        "name": "Postmark",
        "description": "DIY Poker Solver",
        "url": "https://github.com/aaronjsmith4328/Postmark",
    },
]

BLOG_POSTS = [
    {
        "title": "Building my own SPICE Simulator and 31 days of PumpkynSPICE",
        "date": "Sep 3, 2026",
        "url": "https://asmithblogs.bearblog.dev/building-my-own-spice-simulator-and-31-days-of-pumpkynspice/",
    },
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Home",
        social=SOCIAL_LINKS,
        projects=PROJECTS,
        posts=BLOG_POSTS,
    )


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
