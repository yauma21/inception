# Inception example

This is an example of a system for automatically creating pipelines that was created in order to create a
video of it working, rather than as an example of good code for such a system.
It isn't intended to be used for anything real, or to be a particularly good example.
It has been deliberately kept short and simple.

# Install various requirements

You need to install Python, some python modules (see requirements.txt)
and [GoCD version 14.2.0(377-d8a2866d6af85e)](http://www.go.cd/download/).

This example requires running GoCD server and agent on your machine.

You might want to use a VM so you don't have to install these things on your machine.

I might provide a Dockerfile if I get the time.

## Set up inception pipeline

Run: `python create_inception_pipeline.py`

Note that this will run a scripts from my GitHub account - so don't run it until you have
read the code and understood what it is doing.

## See what it does

View [http://localhost:8153](http://localhost:8153).
