--- 
title: Cordova Geolocation Plugin with Ionic 2 and ngRx 
---

<p>The other day I was installing the Cordova Geolocation plugin on an Ionic2 implementing Redux app I have. The issue I was having, was storing the “geolocation" object returned from the Geolocation.getCurrentLocation() method. </p>

<p>The object looks like this:</p>

{% highlight javascript %}console.log(Geolocation.getCurrentLocation()); 
// Geolocation{coords: Coordinates{latitude: #number here, longitude: #number here, accuracy: #number here….}, timestamp: number here}
{% endhighlight %}

<p>It seemed straight forward at first, take the object and through my reducer, assign it to the store.  I did that, but would always end up with an empty object instead of the output object.</p>

<p>What was happening, is that the when using Object.assign with the Geoposition object, the object assign would “lose” the data. Nothing would turn up in the reducer.  Only an empty object.</p>

<p>Therefore, I had to go back to self assigning in my reducer store.</p>

<p> Here is the code: </p>

<p>location.reducer.ts</p>
{% highlight javascript %}export function reducer(state = initialState, action: locationActions.Actions): LocationState {
    switch (action.type) {
        case locationActions.ActionTypes.GET_GPS_LOCATION: {

            return Object.assign({}, state, <LocationState>{
                isLoading: true
            })
        };
        case locationActions.ActionTypes.GET_GPS_LOCATION_SUCCESS: {

            let location: GeoLocationData =  action.locationData;
            const locationStateObj = {
                latitude: location.latitude,
                longitude: location.longitude,
                accuracy: location.accuracy
            }

            return Object.assign({}, state, <LocationState>{
                isLoading: false,
                currentLocData: locationStateObj,
                error: null
            });
        };
        case locationActions.ActionTypes.GET_GPS_LOCATION_FAIL: {
            let error = action.error;

            console.error(error);

            return Object.assign({}, state, <LocationState>{
                isLoading: false,
                error: error
            });
        };

        default:
            return state;
    };
}
{% endhighlight %}
<p>location.effects.ts</p>
{% highlight javascript %}export interface GeolocationResp {
    timestamp: number;
    coords: GeoLocationData;
}

@Injectable()
export class LocationEffects {
    constructor(
        private actions$: Actions,
        private locationService: LocationService
    ) { }

    @Effect() getGpsLocation$: Observable<Action> = this.actions$
        .ofType(locationActions.ActionTypes.GET_GPS_LOCATION)
        .switchMap(() => {
            return this.locationService.getCurrentPosition()
                .map((resp: Geoposition) => this.locationService.checkPositionAccuracy(resp))
                .map(resp => new locationActions.GetGpsLocationSuccess(resp))
                .catch(error => Observable.of(new locationActions.GetGpsLocationFail(error)))
        })        
        .catch(error => Observable.of(new locationActions.GetGpsLocationFail(error)))
{% endhighlight %}

<p>location.service.ts</p>
{% highlight javascript %}@Injectable()
export class LocationService {

    public getCurrentPosition(): Observable<any>{
        return Observable.fromPromise<any>(Geolocation.getCurrentPosition());
    }
}
{% endhighlight %}
<p>locationresponse.service.ts</p>
{% highlight javascript %}public static geolocationToApp(geopositionObj:Geoposition): Geoposition{
    let geoposition = geopositionObj.coords;
    let time = geopositionObj.timestamp;
    return {
        coords:{
            latitude: geoposition.latitude,
            longitude: geoposition.longitude,
            altitude: geoposition.altitude,
            altitudeAccuracy: geoposition.altitudeAccuracy,
            heading: geoposition.heading,
            accuracy: geoposition.accuracy,
            speed: geoposition.speed
        },
        timestamp: time
    }
}

public static mapPositionErrorMessage(errorMessage: PositionError): PositionError[]{
    return [{
        code: errorMessage.code,
        message: errorMessage.message
    }]
}
{% endhighlight %}

