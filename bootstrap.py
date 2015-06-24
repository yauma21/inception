import sys
from gomatic import GoCdConfigurator, HostRestClient, ExecTask

configurator = GoCdConfigurator(HostRestClient("localhost:8153"))

pipeline_name = sys.argv[1]

pipeline = configurator\
    .ensure_pipeline_group("auto-created")\
    .find_pipeline(pipeline_name)

for stage in pipeline.stages()[1:]:
    pipeline.ensure_removal_of_stage(stage.name())

commands = open("commands.txt").readlines()
for command in commands:
    command_name, thing_to_execute = command.strip().split('=')
    pipeline\
        .ensure_stage(command_name)\
        .ensure_job(command_name)\
        .ensure_task(ExecTask(thing_to_execute.split(" ")))

configurator.save_updated_config()
