# Fitness trackers
## Using
A fitness tracker module built in pure Python using OPP. Depending on the type of workout and other data, the module calculates the number of calories burned and the distance traveled. It can be easily integrated into a project.

To use the tracker you need to call
```sh
read_package(workout_abbreviation: str, data_list: list)
```

Works with three types of workouts - swimming(SWM), running(RUN) and walking(WLK). Can be easily expanded with new types of workouts. To do this, you can inherit from the base class `Training`. Don't forget to extend dict `training_type` in `read_package` func.

## License

MIT

**Free Software, Hell Yeah!**
