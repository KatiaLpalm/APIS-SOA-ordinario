package com.example.apartamentos.controllers;

import com.example.apartamentos.models.Mensaje;
import com.example.apartamentos.services.MensajeService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/mensajes")
@CrossOrigin(origins = "*")
public class MensajeController {

    private final MensajeService mensajeService;

    public MensajeController(MensajeService mensajeService) {
        this.mensajeService = mensajeService;
    }

    @GetMapping
    public List<Mensaje> getAllMensajes() {
        return mensajeService.getAllMensajes();
    }

    @GetMapping("/{id}")
    public Optional<Mensaje> getMensajeById(@PathVariable Integer id) {
        return mensajeService.getMensajeById(id);
    }

    @PostMapping
    public Mensaje saveMensaje(@RequestBody Mensaje mensaje) {
        return mensajeService.saveMensaje(mensaje);
    }

    @DeleteMapping("/{id}")
    public void deleteMensaje(@PathVariable Integer id) {
        mensajeService.deleteMensaje(id);
    }
}
