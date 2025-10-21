package com.example.apartamentos.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.apartamentos.models.Disponibilidad;
import com.example.apartamentos.repositories.IDisponibilidadRepository;

@Service
public class DisponibilidadService {

    @Autowired
    private IDisponibilidadRepository disponibilidadRepository;

    public List<Disponibilidad> getAllDisponibilidades() {
        return disponibilidadRepository.findAll();
    }

    public Optional<Disponibilidad> getDisponibilidadById(Long id) {
        return disponibilidadRepository.findById(id);
    }

    public Disponibilidad saveDisponibilidad(Disponibilidad disponibilidad) {
        return disponibilidadRepository.save(disponibilidad);
    }

    public void deleteDisponibilidad(Long id) {
        disponibilidadRepository.deleteById(id);
    }
}
