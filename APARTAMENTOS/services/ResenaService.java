package com.example.apartamentos.services;

import com.example.apartamentos.models.IResenaRepository;
import com.example.apartamentos.models.Resena;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ResenaService {

    @Autowired
    private IResenaRepository resenaRepo;

   
    public List<Resena> getAllResenas() {
        return resenaRepo.findAll();
    }

    
    public Optional<Resena> getResenaById(Integer id) {
        return resenaRepo.findById(id);
    }

   
    public Resena saveResena(Resena resena) {
        return resenaRepo.save(resena);
    }

    
    public void deleteResena(Integer id) {
        resenaRepo.deleteById(id);
    }
}
