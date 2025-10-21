package com.example.apartamentos.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.apartamentos.models.Disponibilidad;
import com.example.apartamentos.services.DisponibilidadService;

@RestController
@RequestMapping("/api/disponibilidad")
@CrossOrigin(origins = "*")
public class DisponibilidadController {

    @Autowired
    private DisponibilidadService disponibilidadService;

    @GetMapping
    public List<Disponibilidad> getAllDisponibilidades() {
        return disponibilidadService.getAllDisponibilidades();
    }

    @GetMapping("/{id}")
    public Optional<Disponibilidad> getDisponibilidadById(@PathVariable Long id) {
        return disponibilidadService.getDisponibilidadById(id);
    }

    @PostMapping
    public Disponibilidad saveDisponibilidad(@RequestBody Disponibilidad disponibilidad) {
        return disponibilidadService.saveDisponibilidad(disponibilidad);
    }

    @DeleteMapping("/{id}")
    public void deleteDisponibilidad(@PathVariable Long id) {
        disponibilidadService.deleteDisponibilidad(id);
    }
}
