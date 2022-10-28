## How to use

There is a Makefile in the root of the repo than can be used to build and deploy the solution.

To build individual projects run:

```
make compose-build-backend

or

make compose-build-frontend
```

To build and run individual projects run:
```
make compose-run-backend

or

make compose-run-frontend
```

To build the project run:
```
make compose-build

```

To build and run the project run:
```
make compose-up

```

To remove the solution run:
```
make compose-up-down

```

###Note
Remember to populate your `.env.local` file in the `frontend` directory in you want to point to a custom backend API Url endpoint.
