package moe.izz.httpstefano.spark;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.os.Bundle;
import android.os.RemoteException;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.kontakt.sdk.android.configuration.ForceScanConfiguration;
import com.kontakt.sdk.android.configuration.MonitorPeriod;
import com.kontakt.sdk.android.connection.OnServiceBoundListener;
import com.kontakt.sdk.android.device.Beacon;
import com.kontakt.sdk.android.device.Region;
import com.kontakt.sdk.android.manager.BeaconManager;

import java.util.List;

public class Spark extends Activity {

    private static final int REQUEST_CODE_ENABLE_BLUETOOTH = 1;

    private BeaconManager beaconManager;
    private Beacon beacon;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spark);


        beaconManager = BeaconManager.newInstance(this);
        beaconManager.registerRangingListener(new BeaconManager.RangingListener() {
            @Override
            public void onBeaconsDiscovered(final Region region, final List<Beacon> beacons) {
                TextView myAwesomeTextView = (TextView)findViewById(R.id.textView1);
                for (Beacon b : beacons){
                   myAwesomeTextView.setText(b.getMacAddress());
                }

            };
                                              });
        TextView myAwesomeTextView = (TextView)findViewById(R.id.textView1);
        beaconManager.setMonitorPeriod(MonitorPeriod.MINIMAL);
        beaconManager.setForceScanConfiguration(ForceScanConfiguration.DEFAULT);
        beaconManager.registerMonitoringListener(new BeaconManager.MonitoringListener() {
            @Override
            public void onMonitorStart() {}

            @Override
            public void onMonitorStop() {

            }

            @Override
            public void onBeaconsUpdated(final Region region, final List<Beacon> beacons) {
                TextView myAwesomeTextView = (TextView)findViewById(R.id.textView1);
                for (Beacon b : beacons){
                    myAwesomeTextView.setText(b.getMacAddress());
                }

            }

            @Override
            public void onBeaconAppeared(final Region region, final Beacon beacon) {
                TextView myAwesomeTextView = (TextView)findViewById(R.id.textView1);
                myAwesomeTextView.setText(beacon.getMacAddress()+"gogogogo");


            }

            @Override
            public void onRegionEntered(final Region region) {
               // String macAddress = beacon.getMacAddress().toCharArray().toString();
                //myAwesomeTextView.setText(macAdress);
            }

            @Override
            public void onRegionAbandoned(final Region region) {

            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        if(!beaconManager.isBluetoothEnabled()) {
            final Intent intent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(intent, REQUEST_CODE_ENABLE_BLUETOOTH);
        } else {
            connect();
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        beaconManager.stopMonitoring();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        beaconManager.disconnect();
        beaconManager = null;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {

        if(requestCode == REQUEST_CODE_ENABLE_BLUETOOTH) {
            if(resultCode == Activity.RESULT_OK) {
                connect();
            } else {
                Toast.makeText(this, "Bluetooth not enabled", Toast.LENGTH_LONG).show();
                getActionBar().setSubtitle("Bluetooth not enabled");
            }
            return;
        }

        super.onActivityResult(requestCode, resultCode, data);
    }

    private void connect() {
        try {
            beaconManager.connect(new OnServiceBoundListener() {
                @Override
                public void onServiceBound() throws RemoteException {
                    beaconManager.startRanging(Region.EVERYWHERE);
                    Log.d("FCUK", "hfsdjakf");
                }
            });
        } catch (RemoteException e) {

        }
    }

    }
