package com.example.cursocomputervision

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem

/* R é a referencia para a pasta 'res' */

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    // cria o menu
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu, menu)

        return super.onCreateOptionsMenu(menu)
    }

    // trata os eventos de clique nos botões do menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val id = item.itemId

        if(id == R.id.action_exit) {
            finish()
        }
        else if(id == R.id.action_photo) {

        }
        else if(id == R.id.action_save) {

        }

        return super.onOptionsItemSelected(item)
    }
}