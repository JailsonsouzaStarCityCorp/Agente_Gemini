// JavaScript personalizado para o Sistema de Agentes de IA

// Utilitários gerais
const App = {
    // Inicialização
    init: function() {
        this.setupEventListeners();
        this.initializeComponents();
    },

    // Configurar event listeners
    setupEventListeners: function() {
        // Auto-hide alerts
        setTimeout(() => {
            const alerts = document.querySelectorAll('.alert');
            alerts.forEach(alert => {
                if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
                    alert.style.transition = 'opacity 0.5s ease';
                    alert.style.opacity = '0';
                    setTimeout(() => alert.remove(), 500);
                }
            });
        }, 5000);

        // Smooth scrolling para links internos
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    },

    // Inicializar componentes
    initializeComponents: function() {
        // Adicionar animações de fade-in
        const cards = document.querySelectorAll('.card');
        cards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.1}s`;
            card.classList.add('fade-in');
        });

        // Inicializar tooltips do Bootstrap
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    },

    // Utilitários de API
    api: {
        // Fazer requisição GET
        get: async function(url) {
            try {
                const response = await fetch(url);
                return await response.json();
            } catch (error) {
                console.error('Erro na requisição GET:', error);
                throw error;
            }
        },

        // Fazer requisição POST
        post: async function(url, data) {
            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });
                return await response.json();
            } catch (error) {
                console.error('Erro na requisição POST:', error);
                throw error;
            }
        }
    },

    // Utilitários de UI
    ui: {
        // Mostrar loading
        showLoading: function(element, text = 'Carregando...') {
            element.innerHTML = `
                <div class="text-center py-4">
                    <i class="fas fa-spinner fa-spin fa-2x text-primary mb-3"></i>
                    <p class="text-muted">${text}</p>
                </div>
            `;
        },

        // Mostrar erro
        showError: function(element, message) {
            element.innerHTML = `
                <div class="alert alert-danger">
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    ${message}
                </div>
            `;
        },

        // Mostrar sucesso
        showSuccess: function(element, message) {
            element.innerHTML = `
                <div class="alert alert-success">
                    <i class="fas fa-check-circle me-2"></i>
                    ${message}
                </div>
            `;
        },

        // Copiar texto para clipboard
        copyToClipboard: async function(text) {
            try {
                await navigator.clipboard.writeText(text);
                return true;
            } catch (error) {
                console.error('Erro ao copiar:', error);
                return false;
            }
        },

        // Mostrar notificação toast
        showToast: function(message, type = 'info') {
            const toastContainer = document.getElementById('toast-container') || this.createToastContainer();
            
            const toast = document.createElement('div');
            toast.className = `toast align-items-center text-white bg-${type} border-0`;
            toast.setAttribute('role', 'alert');
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            `;
            
            toastContainer.appendChild(toast);
            
            const bsToast = new bootstrap.Toast(toast);
            bsToast.show();
            
            // Remover toast após ser escondido
            toast.addEventListener('hidden.bs.toast', () => {
                toast.remove();
            });
        },

        // Criar container de toasts
        createToastContainer: function() {
            const container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container position-fixed top-0 end-0 p-3';
            container.style.zIndex = '9999';
            document.body.appendChild(container);
            return container;
        }
    },

    // Utilitários de validação
    validation: {
        // Validar email
        isValidEmail: function(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        },

        // Validar se campo não está vazio
        isNotEmpty: function(value) {
            return value && value.trim().length > 0;
        },

        // Validar tamanho mínimo
        hasMinLength: function(value, minLength) {
            return value && value.length >= minLength;
        }
    },

    // Utilitários de formatação
    format: {
        // Formatar data
        formatDate: function(date) {
            return new Date(date).toLocaleDateString('pt-BR');
        },

        // Formatar data e hora
        formatDateTime: function(date) {
            return new Date(date).toLocaleString('pt-BR');
        },

        // Formatar moeda
        formatCurrency: function(value) {
            return new Intl.NumberFormat('pt-BR', {
                style: 'currency',
                currency: 'BRL'
            }).format(value);
        },

        // Formatar número
        formatNumber: function(value) {
            return new Intl.NumberFormat('pt-BR').format(value);
        }
    }
};

// Funções específicas para o chat
const Chat = {
    // Adicionar mensagem ao chat
    addMessage: function(message, isUser = false) {
        const chatMessages = document.getElementById('chat-messages');
        if (!chatMessages) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        const now = new Date().toLocaleTimeString();
        
        messageDiv.innerHTML = `
            <div class="d-flex align-items-start">
                <div class="avatar me-3">
                    <i class="fas fa-${isUser ? 'user' : 'robot'} fa-2x text-${isUser ? 'secondary' : 'primary'}"></i>
                </div>
                <div class="message-content">
                    <div class="message-bubble ${isUser ? 'bg-primary text-white' : 'bg-light'} p-3 rounded">
                        <p class="mb-0">${message}</p>
                    </div>
                    <small class="text-muted">${now}</small>
                </div>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    },

    // Limpar chat
    clear: function() {
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages) {
            chatMessages.innerHTML = `
                <div class="message bot-message">
                    <div class="d-flex align-items-start">
                        <div class="avatar me-3">
                            <i class="fas fa-robot fa-2x text-primary"></i>
                        </div>
                        <div class="message-content">
                            <div class="message-bubble bg-light p-3 rounded">
                                <p class="mb-0">Chat limpo! Como posso te ajudar?</p>
                            </div>
                            <small class="text-muted">Agora</small>
                        </div>
                    </div>
                </div>
            `;
        }
    }
};

// Funções específicas para o dashboard
const Dashboard = {
    // Atualizar estatísticas
    updateStats: async function() {
        try {
            const data = await App.api.get('/api/estatisticas');
            if (data.sucesso) {
                this.updateStatsCards(data.dados);
                this.updateCharts(data.dados);
            }
        } catch (error) {
            console.error('Erro ao atualizar estatísticas:', error);
        }
    },

    // Atualizar cards de estatísticas
    updateStatsCards: function(stats) {
        const elements = {
            'total-processamentos': stats.processamentos?.total || 0,
            'total-sucessos': stats.processamentos?.sucessos || 0,
            'total-erros': stats.processamentos?.erros || 0,
            'taxa-sucesso': `${(stats.processamentos?.taxa_sucesso || 0).toFixed(1)}%`
        };

        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        });
    },

    // Atualizar gráficos
    updateCharts: function(stats) {
        // Implementar atualização de gráficos se necessário
        console.log('Atualizando gráficos com:', stats);
    }
};

// Funções específicas para conteúdo
const Content = {
    // Copiar conteúdo gerado
    copyContent: async function() {
        const contentElement = document.querySelector('.conteudo-texto');
        if (!contentElement) return;

        const success = await App.ui.copyToClipboard(contentElement.textContent);
        if (success) {
            App.ui.showToast('Conteúdo copiado para a área de transferência!', 'success');
        } else {
            App.ui.showToast('Erro ao copiar conteúdo', 'danger');
        }
    },

    // Salvar conteúdo
    saveContent: function() {
        const contentElement = document.querySelector('.conteudo-texto');
        if (!contentElement) return;

        const blob = new Blob([contentElement.textContent], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `conteudo_${new Date().toISOString().slice(0, 10)}.txt`;
        a.click();
        URL.revokeObjectURL(url);
        
        App.ui.showToast('Conteúdo salvo com sucesso!', 'success');
    }
};

// Inicializar aplicação quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    App.init();
    
    // Inicializar componentes específicos baseados na página
    const currentPage = window.location.pathname;
    
    if (currentPage.includes('/dashboard')) {
        Dashboard.updateStats();
        // Atualizar dashboard a cada 30 segundos
        setInterval(Dashboard.updateStats, 30000);
    }
    
    if (currentPage.includes('/suporte')) {
        // Configurações específicas do chat
        console.log('Página de suporte carregada');
    }
    
    if (currentPage.includes('/conteudo')) {
        // Configurações específicas de conteúdo
        console.log('Página de conteúdo carregada');
    }
});

// Exportar para uso global
window.App = App;
window.Chat = Chat;
window.Dashboard = Dashboard;
window.Content = Content;
