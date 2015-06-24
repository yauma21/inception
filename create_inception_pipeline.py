from gomatic import GoCdConfigurator, HostRestClient, ExecTask, GitMaterial

configurator = GoCdConfigurator(HostRestClient("docker:8153"))

pipeline = configurator\
    .ensure_pipeline_group("inception")\
    .ensure_replacement_of_pipeline("inception")\
    .set_git_material(GitMaterial("https://github.com/yauma21/inception.git",
                                  polling=False))\
    .set_timer("0 0 * * * ?")  # run on the hour, every hour
inception_job = pipeline.ensure_stage("inception").ensure_job("inception")
inception_job.ensure_task(ExecTask(["python", "inception.py"]))

configurator.save_updated_config()
